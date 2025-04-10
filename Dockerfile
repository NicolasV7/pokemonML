FROM python:3.9-slim as builder

WORKDIR /app

ARG FLASK_ENV
ARG SECRET_KEY
ARG MODEL_PATH

ENV FLASK_ENV=${FLASK_ENV}
ENV SECRET_KEY=${SECRET_KEY}
ENV MODEL_PATH=${MODEL_PATH}

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY . .

ENV PYTHONPATH=/app
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PATH="/root/.local/bin:${PATH}"

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "120", "app:create_app()"]
from flask import Blueprint, current_app, render_template, request
from services.predict_service import PredictorService

bp = Blueprint('predict', __name__)

# Inicializar servicio con la app
def init_service(app):
    global service
    service = PredictorService(app)

@bp.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            stats = [
                float(request.form['hp']),
                float(request.form['attack']),
                float(request.form['defense']),
                float(request.form['sp_atk']),
                float(request.form['sp_def']),
                float(request.form['speed'])
            ]

            cluster, examples = service.predict_cluster(stats)
            return render_template('index.html',
                                prediction=cluster,
                                examples=examples)

        except Exception as e:
            return render_template('index.html',
                                error=f"Error: {str(e)}")

    return render_template('index.html')
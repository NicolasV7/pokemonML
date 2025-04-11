from core import create_app

app = create_app()

from routes.predict import init_service
init_service(app)

if __name__ == "__main__":
    app.run(debug=True)
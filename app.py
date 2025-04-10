import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from core.config import Config
from routes.main_routes import configure_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    configure_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
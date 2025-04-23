from flask import Flask
from core.config import Config

def create_app():
    app = Flask(__name__,
                static_folder='../static',
                template_folder='../templates')

    app.config.from_object(Config(app.root_path))

    _register_blueprints(app)

    return app

def _register_blueprints(app):
    from routes.predict_routes import create_predict_blueprint

    predict_bp = create_predict_blueprint(app)
    app.register_blueprint(predict_bp)
from core.config import Config
from flask import Flask # type: ignore
from core.logging import configure_logging, configure_flask_logging

def create_app():
    logger = configure_logging()

    app = Flask(__name__,
                static_folder='../static',
                template_folder='../templates')

    app.config.from_object(Config(app.root_path))

    app = configure_flask_logging(app)

    _register_blueprints(app)

    return app

def _register_blueprints(app):
    from routes.predict_routes import create_predict_blueprint

    predict_bp = create_predict_blueprint(app)
    app.register_blueprint(predict_bp)
import logging
from flask import Blueprint # type: ignore
from rich.panel import Panel # type: ignore
from services.predictor_service import PredictorService
from controllers.predict_controller import PredictController

def create_predict_blueprint(app):
    bp = Blueprint('predict', __name__)
    logger = logging.getLogger(app.name)

    logger.info(Panel.fit(
        "Registrando blueprint de predicción",
        title="[bold]🔮 Predict Routes[/]",
        border_style="magenta"
    ))

    service = PredictorService(app)
    controller = PredictController(service)

    bp.add_url_rule('/',
                   view_func=controller.handle_prediction,
                   methods=['GET', 'POST'])

    return bp
from flask import Blueprint
from controllers.predict_controller import PredictController
from services.predictor_service import PredictorService

def create_predict_blueprint(app):
    bp = Blueprint('predict', __name__)
    service = PredictorService(app)
    controller = PredictController(service)

    # Configura las rutas
    bp.add_url_rule('/',
                   view_func=controller.handle_prediction,
                   methods=['GET', 'POST'])

    return bp
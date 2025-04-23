from flask import jsonify, render_template, request
from services.predictor_service import PredictorService

class PredictController:
    def __init__(self, service: PredictorService):
        self.service = service

    def handle_prediction(self):
        if request.method == 'POST':
            return self._handle_post_request()
        return self._handle_get_request()

    def _handle_post_request(self):
        try:
            stats = self._extract_stats_from_request()
            cluster, examples = self.service.predict_cluster(stats)
            return self._build_success_response(cluster, examples)
        except Exception as e:
            return self._build_error_response(str(e))

    def _extract_stats_from_request(self):
        return [
            float(request.form['hp']),
            float(request.form['attack']),
            float(request.form['defense']),
            float(request.form['sp_atk']),
            float(request.form['sp_def']),
            float(request.form['speed'])
        ]

    def _build_success_response(self, cluster, examples):
        return jsonify({
            'prediction': {
                'nombre': cluster['nombre'],
                'descripcion': cluster['descripcion'],
                'ejemplos': cluster['ejemplos']
            },
            'examples': examples
        })

    def _build_error_response(self, error_message):
        return render_template('index.html', error=f"Error: {error_message}")

    def _handle_get_request(self):
        return render_template('index.html')
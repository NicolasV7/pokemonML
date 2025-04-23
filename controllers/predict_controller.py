import logging
from rich.panel import Panel # type: ignore
from flask import render_template, request # type: ignore

class PredictController:
    def __init__(self, service):
        self.service = service
        self.logger = logging.getLogger('controllers.predict')

    def handle_prediction(self):
        if request.method == 'POST':
            self.logger.info(Panel.fit(
                "Nueva solicitud de predicción recibida",
                border_style="blue"
            ))

            try:
                stats = [
                    float(request.form['hp']),
                    float(request.form['attack']),
                    float(request.form['defense']),
                    float(request.form['sp_atk']),
                    float(request.form['sp_def']),
                    float(request.form['speed'])
                ]

                self.logger.debug(f"Stats recibidos: {stats}")

                cluster, examples = self.service.predict_cluster(stats)

                self.logger.info(Panel.fit(
                    f"Predicción completada - Cluster: {cluster['nombre']}",
                    border_style="green"
                ))

                return {
                    'prediction': {
                        'nombre': cluster['nombre'],
                        'descripcion': cluster['descripcion'],
                        'ejemplos': cluster['ejemplos']
                    },
                    'examples': examples
                }

            except Exception as e:
                self.logger.error(Panel.fit(
                    f"Error en predicción: {str(e)}",
                    border_style="red"
                ))
                return render_template('index.html', error=f"Error: {str(e)}")

        self.logger.debug("Solicitud GET recibida")
        return render_template('index.html')
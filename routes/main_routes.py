from flask import render_template, request
from services.pokemon_service import PokemonService
from core.config import Config

def configure_routes(app):
    service = PokemonService(Config.MODEL_PATH)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        prediction = None
        error = None

        if request.method == 'POST':
            try:
                type1 = request.form['type1']
                type2 = request.form['type2']
                prediction = service.predict_cluster(type1, type2)
            except Exception as e:
                error = str(e)

        return render_template('index.html',
                             prediction=prediction,
                             types=service.types,
                             error=error)
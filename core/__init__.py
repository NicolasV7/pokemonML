from flask import Flask
import os

def create_app():
    app = Flask(__name__,
                static_folder='../static',
                template_folder='../templates')
    app.config.from_mapping(
        MODEL_PATH=os.path.join(app.root_path, '../models/kmeans_model.pkl'),
        SCALER_PATH=os.path.join(app.root_path, '../models/scaler.pkl'),
        DATA_PATH=os.path.join(app.root_path, '../models/pokedex_cluster.csv')
    )

    from routes.predict import bp as predict_bp
    app.register_blueprint(predict_bp)

    return app
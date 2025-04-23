import logging
import pandas as pd # type: ignore
from .resource_service import ResourceService

class PredictorService:
    def __init__(self, app):
        self.app = app
        self.logger = logging.getLogger('services.predictor')
        self.logger.info("Inicializando PredictorService...")
        self.resource_service = ResourceService(app.config)
        self.resource_service.load_all_resources()

    @property
    def model(self):
        return self.resource_service.model

    @property
    def scaler(self):
        return self.resource_service.scaler

    @property
    def df(self):
        return self.resource_service.df

    @property
    def cluster_info(self):
        return self.resource_service.cluster_info

    def predict_cluster(self, stats):
        self.logger.debug("Iniciando predicción de cluster...")
        features = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']

        try:
            input_df = pd.DataFrame([stats], columns=features)
            self.logger.debug(f"Datos de entrada:\n{input_df.to_string()}")

            scaled_data = self.scaler.transform(input_df)

            cluster = self.model.predict(scaled_data)[0]
            self.logger.info(f"📊 Cluster predicho: {cluster}")

            examples_data = self.df[self.df['Clusters'] == cluster][['#', 'Name']].sample(3)
            examples = [{
                'name': row['Name'],
                'image': f"{row['#']:03d}.png"
            } for _, row in examples_data.iterrows()]

            self.logger.debug(f"Ejemplos encontrados: {examples}")

            return self.cluster_info[cluster], examples

        except Exception as e:
            self.logger.error(f"Error en predict_cluster: {str(e)}", exc_info=True)
            raise

    def __init__(self, app):
        self.app = app
        self.resource_service = ResourceService(app.config)
        self.resource_service.load_all_resources()

    @property
    def model(self):
        return self.resource_service.model

    @property
    def scaler(self):
        return self.resource_service.scaler

    @property
    def df(self):
        return self.resource_service.df

    @property
    def cluster_info(self):
        return self.resource_service.cluster_info

    def predict_cluster(self, stats):
        features = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
        input_df = pd.DataFrame([stats], columns=features)

        scaled_data = self.scaler.transform(input_df)
        cluster = self.model.predict(scaled_data)[0]

        examples_data = self.df[self.df['Clusters'] == cluster][['#', 'Name']].sample(3)
        examples = [{
            'name': row['Name'],
            'image': f"{row['#']:03d}.png"
        } for _, row in examples_data.iterrows()]

        return self.cluster_info[cluster], examples
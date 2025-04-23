import pandas as pd # type: ignore
from .resource_service import ResourceService

class PredictorService:
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
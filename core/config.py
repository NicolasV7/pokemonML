import os

class Config:
    def __init__(self, root_path):
        self.MODEL_PATH = os.path.join(root_path, '../models/kmeans_model.pkl')
        self.SCALER_PATH = os.path.join(root_path, '../models/scaler.pkl')
        self.DATA_PATH = os.path.join(root_path, '../models/pokedex_cluster.csv')
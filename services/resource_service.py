import pickle
import pandas as pd # type: ignore
from core.cluster_config import BASE_CLUSTER_INFO

class ResourceService:
    def __init__(self, config):
        self.config = config
        self.model = None
        self.scaler = None
        self.df = None
        self.cluster_info = None

    def load_model(self):
        with open(self.config['MODEL_PATH'], 'rb') as f:
            self.model = pickle.load(f)

    def load_scaler(self):
        with open(self.config['SCALER_PATH'], 'rb') as f:
            self.scaler = pickle.load(f)

    def load_data(self):
        self.df = pd.read_csv(self.config['DATA_PATH'])

    def process_cluster_info(self):
        self.cluster_info = BASE_CLUSTER_INFO.copy()

        for cluster_id in self.cluster_info:
            ejemplos_con_imagenes = []
            for name in self.cluster_info[cluster_id]['ejemplos']:
                pokemon = self.df[self.df['Name'] == name]
                if not pokemon.empty:
                    numero = pokemon.iloc[0]['#']
                    ejemplos_con_imagenes.append({
                        'name': name,
                        'image': f"{numero:03d}.png"
                    })
            self.cluster_info[cluster_id]['ejemplos'] = ejemplos_con_imagenes

    def load_all_resources(self):
        try:
            self.load_model()
            self.load_scaler()
            self.load_data()
            self.process_cluster_info()
            return True
        except Exception as e:
            raise
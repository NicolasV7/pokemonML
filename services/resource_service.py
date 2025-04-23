import pickle
import logging
import pandas as pd # type: ignore
from core.cluster_config import BASE_CLUSTER_INFO

class ResourceService:
    def __init__(self, config):
        self.config = config
        self.model = None
        self.scaler = None
        self.df = None
        self.cluster_info = None
        self.logger = logging.getLogger('services.resource')

    def load_model(self):
        self.logger.debug("Cargando modelo KMeans...")
        with open(self.config['MODEL_PATH'], 'rb') as f:
            self.model = pickle.load(f)
        self.logger.info("✅ Modelo KMeans cargado correctamente")

    def load_scaler(self):
        self.logger.debug("Cargando scaler...")
        with open(self.config['SCALER_PATH'], 'rb') as f:
            self.scaler = pickle.load(f)
        self.logger.info("✅ Scaler cargado correctamente")

    def load_data(self):
        self.logger.debug("Cargando dataset Pokémon...")
        self.df = pd.read_csv(self.config['DATA_PATH'])
        self.logger.info(f"✅ Dataset cargado correctamente (registros: {len(self.df)})")

    def process_cluster_info(self):
        self.logger.debug("Procesando información de clusters...")
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

        self.logger.info("✅ Información de clusters procesada")

    def load_all_resources(self):
        try:
            self.logger.info("Iniciando carga de recursos...")
            self.load_model()
            self.load_scaler()
            self.load_data()
            self.process_cluster_info()
            self.logger.info("🎉 Todos los recursos cargados exitosamente")
            return True
        except Exception as e:
            self.logger.error(f"❌ Error cargando recursos: {str(e)}", exc_info=True)
            raise
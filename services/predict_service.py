import pickle
import pandas as pd
import numpy as np

class PredictorService:
    def __init__(self, app):
        self.app = app
        self.model = None
        self.scaler = None
        self.df = None
        self.cluster_info = {}
        self.load_resources()

    def load_resources(self):
        try:
            # Cargar modelos con rutas absolutas
            with open(self.app.config['MODEL_PATH'], 'rb') as f:
                self.model = pickle.load(f)

            with open(self.app.config['SCALER_PATH'], 'rb') as f:
                self.scaler = pickle.load(f)

            # Cargar datos
            self.df = pd.read_csv(self.app.config['DATA_PATH'])

            self.cluster_info = {
                0: {
                    "nombre": "Equilibrados Tácticos",
                    "descripcion": "Balance ofensivo/defensivo. HP: 70-90, Ataque/Defensa: 80-100",
                    "ejemplos": ["Charizard", "Blastoise", "Venusaur", "Nidoking", "Arcanine"]
                },
                1: {
                    "nombre": "Muros Defensivos",
                    "descripcion": "Altas defensas (>100) y HP (>90). Baja velocidad (<50)",
                    "ejemplos": ["Snorlax", "Steelix", "Aggron", "Umbreon", "Metagross"]
                },
                2: {
                    "nombre": "Velocistas Ofensivos",
                    "descripcion": "Velocidad >110. Ataque/Sp. Atk >100. Defensa baja (<70)",
                    "ejemplos": ["Jolteon", "Aerodactyl", "Crobat", "Weavile", "Ninjask"]
                },
                3: {
                    "nombre": "Defensores Especiales",
                    "descripcion": "Sp. Def >100. HP >90. Buen balance defensivo",
                    "ejemplos": ["Alakazam", "Slowking", "Muk", "Cresselia", "Mr. Mime"]
                },
                4: {
                    "nombre": "Legendarios Puros",
                    "descripcion": "Stats totales >600. Múltiples stats >100",
                    "ejemplos": ["Mewtwo", "Lugia", "Rayquaza", "Groudon", "Kyogre"]
                }
            }

            print("✅ Recursos cargados exitosamente")
        except Exception as e:
            print(f"❌ Error cargando recursos: {str(e)}")
            raise

    def predict_cluster(self, stats):
        # Preprocesamiento
        features = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
        input_df = pd.DataFrame([stats], columns=features)

        # Escalado y predicción
        scaled_data = self.scaler.transform(input_df)
        cluster = self.model.predict(scaled_data)[0]

        # Obtener ejemplos reales
        examples = self.df[self.df['Clusters'] == cluster]['Name'].sample(3).tolist()

        return self.cluster_info[cluster], examples
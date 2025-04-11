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
                    "nombre": "Weakest Pokemons Cluster",
                    "descripcion": "The weakest Pokemons, low values for all the Skills",
                    "ejemplos": ["Magikarp", "Porygon", "Magikarp"]
                },
                1: {
                    "nombre": "The Overpowering Squad",
                    "descripcion": "The strongest Pokemons have high values for all skills. Speed, Attack and Special Attack are the top 3 skills",
                    "ejemplos": ["AegislashBlade Forme", "KyogrePrimal Kyogre", "MewtwoMega Mewtwo Y"]
                },
                2: {
                    "nombre": "Speedy Squad",
                    "descripcion": "Cluster of the fastest Pokemons. Speed, Attack and Special Attack are the Top 3 Skills",
                    "ejemplos": ["Accelgor", "Ninjask", "Crobat"]
                },
                3: {
                    "nombre": "The Defensive Squad",
                    "descripcion": "The highest Skills are Defense and Special Defense. Defensive, Special Defense and Attack are the Top 3 Skills",
                    "ejemplos": ["Shuckle", "Regirock", "Steelix"]
                },
                4: {
                    "nombre": "High HP and Slow Speed Cluster",
                    "descripcion": "They have High HP and Slow Speed. HP, Attack and Special Defense are the top 3 skills",
                    "ejemplos": ["Blissey", "Chansey", "Wobbuffet"]
                }
            }

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

        # Obtener ejemplos reales con imágenes
        examples_data = self.df[self.df['Clusters'] == cluster][['#', 'Name']].sample(3)
        examples = [{
            'name': row['Name'],
            'image': f"{row['#']:03d}.png"
        } for _, row in examples_data.iterrows()]

        return self.cluster_info[cluster], examples
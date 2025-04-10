import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import joblib

class PokemonService:
    def __init__(self, model_path, encoder_path):
        self.model = joblib.load(model_path)
        self.encoder = joblib.load(encoder_path)
        self.types = [
            'Grass', 'Fire', 'Water', 'Bug', 'Normal', 'Poison',
            'Electric', 'Ground', 'Fairy', 'Fighting', 'Psychic',
            'Rock', 'Ghost', 'Ice', 'Dragon', 'Dark', 'Steel', 'Flying'
        ]

    def preprocess_input(self, type1, type2):
        input_df = pd.DataFrame([[type1, type2]], columns=['Type1', 'Type2'])
        return self.encoder.transform(input_df)

    def predict_cluster(self, type1, type2):
        try:
            features = self.preprocess_input(type1, type2)
            return self.model.predict(features)[0]
        except Exception as e:
            raise ValueError(f"Error: {str(e)}")
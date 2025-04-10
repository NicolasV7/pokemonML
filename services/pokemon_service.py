import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

class PokemonService:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)
        self.types = ['Grass', 'Fire', 'Water', 'Bug', 'Normal', 'Poison',
                     'Electric', 'Ground', 'Fairy', 'Fighting', 'Psychic',
                     'Rock', 'Ghost', 'Ice', 'Dragon', 'Dark', 'Steel', 'Flying']
        self.encoder = OneHotEncoder(handle_unknown='ignore')

    def load_model(self, path):
        with open(path, 'rb') as file:
            return pickle.load(file)

    def preprocess_input(self, type1, type2):
        input_df = pd.DataFrame([[type1, type2]], columns=['Type1', 'Type2'])
        return pd.get_dummies(input_df, columns=['Type1', 'Type2'])

    def predict_cluster(self, type1, type2):
        try:
            features = self.preprocess_input(type1, type2)
            return self.model.predict(features)[0]
        except Exception as e:
            raise ValueError(f"Prediction error: {str(e)}")
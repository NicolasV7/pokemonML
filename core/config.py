import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/modelo_clasificador.pkl')
    ENCODER_PATH = os.getenv('ENCODER_PATH', 'models/encoder.pkl')
    SECRET_KEY = os.getenv('SECRET_KEY', 'pokemon-key-123')
from django.apps import AppConfig
from keras.models import load_model
import os

class UsersConfig(AppConfig):
    name = 'users'
    BASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'trained_model.h5')
    MODEL = load_model('trained_model.h5')

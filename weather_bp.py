from pprint import pprint
import openweathermapy.core as owm
from config import api_key

def get_weather():
    settings = {"units": "imperial", "appid": api_key}
    zip_weather = owm.get_current(zip = zip, **settings)
    pprint(zip_weather)
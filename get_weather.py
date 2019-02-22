import openweathermapy.core as owm
from config import weather_api_key


def get_weather(zip_code):
    """
    gets all current weather data from a zip code

    Arguments:
        zip_code {int} -- zip code of interest

    Returns:
        dict -- weather data
    """

    settings = {"units": "imperial", "appid": api_key}
    zip_weather = owm.get_current(zip=zip_code, **settings)
    return zip_weather

# weather_providers.py
import requests
import pandas as pd
import json
from Interfaces.Interfaces import IWeatherProvider
from Models.WeatherForecastModel import WeatherForecastModel


class OpenWeatherMapProvider_v2(IWeatherProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.weather_url = "https://api.openweathermap.org/data/3.0/onecall"

    def get_current_weather(self, lat: float, lon: float) -> WeatherForecastModel:
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.weather_url, params=params)
        json_data = response.json()

        # Parse the JSON data
        #arsed_data = json.loads(json_data)

        # Create DataFrame
        df = pd.DataFrame([json_data])

        if response.status_code == 200:
            temperature = json_data['main']['temp']
            forecast_description = json_data['weather'][0]['description']
            return WeatherForecastModel(city=json_data['name'], temperature=temperature, forecast=forecast_description)
        else:
            raise Exception(f"Błąd podczas pobierania pogody na podstawie koordynatów")




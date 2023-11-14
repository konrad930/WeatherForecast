# weather_providers.py
import requests
from Interfaces.Interfaces import IWeatherProvider
from Models.WeatherForecastModel import WeatherForecastModel


class TomorrowWeatherProvider(IWeatherProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.weather_url = "https://api.tomorrow.io/v4/weather/forecast"

    def get_current_weather(self, lat: float, lon: float) -> WeatherForecastModel:
        params = {
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.weather_url, params=params)
        data = response.json()
        if response.status_code == 200:
            temperature = data['main']['temp']
            forecast_description = data['weather'][0]['description']
            return WeatherForecastModel(city=data['name'], temperature=temperature, forecast=forecast_description)
        else:
            raise Exception(f"Błąd podczas pobierania pogody na podstawie koordynatów")



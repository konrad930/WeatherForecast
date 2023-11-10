# weather_providers.py
import requests
from Interfaces.Interfaces import IWeatherProvider
from Models.WeatherForecastModel import WeatherForecastModel
from typing import Optional

class OpenWeatherMapProvider(IWeatherProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.weather_url = "http://api.openweathermap.org/data/2.5/weather"
        self.geo_url = "http://api.openweathermap.org/geo/1.0/direct"
    def get_coordinates(self, city: str) -> tuple:
        params = {
            'q': city,
            'limit': 1,
            'appid': self.api_key
        }
        response = requests.get(self.geo_url, params=params)
        data = response.json()

        if response.status_code == 200 and data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            return lat, lon
        else:
            raise Exception(f"Nie udało się uzyskać współrzędnych dla {city}")

    def get_weather_by_coordinates(self, lat: float, lon: float) -> WeatherForecastModel:
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


    def get_current_weather(self, location: str) -> Optional[WeatherForecastModel]:
        try:
            params = {'q': location, 'appid': self.api_key, 'units': 'metric'}
            response = requests.get(self.weather_url, params=params)

            if response.status_code == 200:
                data = response.json()
                temperature = data['main']['temp']
                forecast_description = data['weather'][0]['description']
                return WeatherForecastModel(city=data['name'], temperature=temperature, forecast=forecast_description)
            else:
                lat, lon = self.get_coordinates(location)
                return self.get_weather_by_coordinates(lat, lon)
        except Exception as e:
            print(f"Błąd podczas pobierania pogody: {e}")
            return None



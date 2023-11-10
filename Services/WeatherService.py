# weather_service.py

from Interfaces.Interfaces import IWeatherProvider, IWeatherRepository
from Models.WeatherForecastModel import WeatherForecastModel

class WeatherService:
    def __init__(self, weather_repo: IWeatherRepository, weather_provider: IWeatherProvider):
        self.weather_repo = weather_repo
        self.weather_provider = weather_provider

    def get_live_weather(self, location: str) -> WeatherForecastModel:
        # Pobieranie aktualnych danych pogodowych z zewnętrznego API
        return self.weather_provider.get_current_weather(location)

    def get_stored_weather(self, city: str) -> WeatherForecastModel:
        # Pobieranie prognozy pogody z bazy danych
        return self.weather_repo.get_forecast(city)

    def add_weather_forecast(self, forecast: WeatherForecastModel) -> None:
        # Dodawanie prognozy pogody do bazy danych
        self.weather_repo.add_forecast(forecast)

    def update_weather_forecast(self, forecast: WeatherForecastModel) -> None:
        # Aktualizacja prognozy pogody w bazie danych
        self.weather_repo.update_forecast(forecast)

    def delete_weather_forecast(self, city: str) -> None:
        # Usuwanie prognozy pogody z bazy danych
        self.weather_repo.delete_forecast(city)
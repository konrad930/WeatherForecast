from abc import ABC, abstractmethod
from typing import List
from Models.WeatherForecastModel import WeatherForecastModel

class IWeatherRepository(ABC):

    @abstractmethod
    def add_forecast(self, forecast: WeatherForecastModel) -> None:
        """
        Dodaje prognozę pogody do repozytorium.
        """
        pass

    @abstractmethod
    def get_forecast(self, city: str) -> WeatherForecastModel:
        """
        Pobiera prognozę pogody dla określonego miasta.
        """
        pass

    @abstractmethod
    def update_forecast(self, forecast: WeatherForecastModel) -> None:
        """
        Aktualizuje istniejącą prognozę pogody w repozytorium.
        """
        pass

    @abstractmethod
    def delete_forecast(self, city: str) -> None:
        """
        Usuwa prognozę pogody dla określonego miasta.
        """
        pass

    @abstractmethod
    def get_all_forecasts(self) -> List[WeatherForecastModel]:
        """
        Zwraca wszystkie prognozy pogody z repozytorium.
        """
        pass

class IGeoLocationProvider(ABC):
    @abstractmethod
    def get_coordinates(self, city: str) -> tuple:
        pass

class IWeatherProvider(ABC):
    @abstractmethod
    def get_current_weather(self, lat: float, lon: float) -> WeatherForecastModel:
        pass

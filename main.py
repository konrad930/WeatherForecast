# main.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Services.WeatherService import WeatherService
from Repostories.SQLAlchemy.WeatherRepositorySQLAlchemy import WeatherRepositorySQLAlchemy
from WeatherProviders.OpenWeatherMapProvider import OpenWeatherMapProvider
from Repostories.SQLAlchemy.WeatherForecastORM import Base
from Models.WeatherForecastModel import WeatherForecastModel

def main():
    # Konfiguracja bazy danych
    engine = create_engine('sqlite:///weather_data.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Tworzenie instancji repozytorium i dostawcy danych pogodowych
    weather_repo = WeatherRepositorySQLAlchemy(session)
    weather_provider = OpenWeatherMapProvider(api_key="5e1ab9a3366d36c486baed1203b6f166")
    # Tworzenie serwisu pogodowego
    weather_service = WeatherService(weather_repo, weather_provider)

    # Pobieranie aktualnej pogody z API
    live_weather = weather_service.get_live_weather("Krakow")
    print("Aktualna pogoda z API:", live_weather)

    # Dodawanie prognozy pogody przez repo
    weather_service.add_weather_forecast(live_weather)

    # READ: Pobieranie prognozy pogody
    stored_forecast = weather_service.get_stored_weather("Krakow")
    print("Pobrano prognozę z bazy danych:", stored_forecast)

    # UPDATE: Aktualizacja prognozy pogody
    stored_forecast = WeatherForecastModel(city="Krakow", temperature=24.0, forecast="light rain")
    weather_service.update_weather_forecast(stored_forecast)
    print("Zaktualizowano prognozę pogody.")

    stored_forecast = weather_service.get_stored_weather("Krakow")
    print("Pobrano prognozę z bazy danych:", stored_forecast)

    # DELETE: Usuwanie prognozy pogody
    weather_service.delete_weather_forecast("Krakow")
    print("Usunięto prognozę pogody.")


if __name__ == "__main__":
    main()

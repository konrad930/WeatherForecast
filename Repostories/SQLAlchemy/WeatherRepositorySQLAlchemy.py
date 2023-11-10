# repository.py
from sqlalchemy.orm import Session
from Models.WeatherForecastModel import WeatherForecastModel
from Interfaces.Interfaces import IWeatherRepository
from Repostories.SQLAlchemy.WeatherForecastORM import WeatherForecastORM
from typing import Optional

class WeatherRepositorySQLAlchemy(IWeatherRepository):
    def __init__(self, session: Session):
        self.session = session

    def add_forecast(self, forecast: WeatherForecastModel) -> None:
        orm_model = WeatherForecastORM(city=forecast.city, temperature=forecast.temperature, forecast=forecast.forecast)
        self.session.add(orm_model)
        self.session.commit()

    def get_forecast(self, city: str) -> Optional[WeatherForecastModel]:
        orm_model = self.session.query(WeatherForecastORM).filter_by(city=city).first()
        if orm_model:
            return WeatherForecastModel(city=orm_model.city, temperature=orm_model.temperature,
                                        forecast=orm_model.forecast)
        return None

    def update_forecast(self, forecast: WeatherForecastModel) -> None:
        orm_model = self.session.query(WeatherForecastORM).filter_by(city=forecast.city).first()
        if orm_model:
            orm_model.temperature = forecast.temperature
            orm_model.forecast = forecast.forecast
            self.session.commit()

    def delete_forecast(self, city: str) -> None:
        orm_model = self.session.query(WeatherForecastORM).filter_by(city=city).first()
        if orm_model:
            self.session.delete(orm_model)
            self.session.commit()

    def get_all_forecasts(self):
        orm_models = self.session.query(WeatherForecastORM).all()
        return [WeatherForecastModel(city=m.city, temperature=m.temperature, forecast=m.forecast) for m in orm_models]

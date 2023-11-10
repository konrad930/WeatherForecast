# orm_models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WeatherForecastORM(Base):
    __tablename__ = 'weather_forecasts'

    id = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    forecast = Column(String, nullable=False)

    def __repr__(self):
        return f"<WeatherForecast(city='{self.city}', temperature={self.temperature}, forecast='{self.forecast}')>"

# models.py

class WeatherForecastModel:
    def __init__(self, city: str, temperature: float, forecast: str):
        self.city = city
        self.temperature = temperature
        self.forecast = forecast

    def __repr__(self):
        return f"WeatherForecastModel(city='{self.city}', temperature={self.temperature}, forecast='{self.forecast}')"

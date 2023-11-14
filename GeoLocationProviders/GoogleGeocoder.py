import requests
from Interfaces.Interfaces import IGeoLocationProvider

class GoogleGeocoder(IGeoLocationProvider):
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    #AIzaSyDG7RkvBdwrFVA6gOCKhgYLR65Zugi0PvI
    def get_coordinates(self, city: str) -> tuple:
        params = {"address": city, "key": self.api_key}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            result = response.json()
            if result["results"]:
                location = result["results"][0]["geometry"]["location"]
                return location["lat"], location["lng"]
            else:
                print("No results found for the specified city.")
                return None
        else:
            print("Error occurred in API request.")
            return None

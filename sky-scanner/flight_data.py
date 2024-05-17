import json
import requests


class FlightData:
    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Duffel-Version": "v1",
            "Content-Type": "application/json",
        }
        self.token = token

    def get_airports(self):
        airports, url = {}, "https://api.duffel.com/air/airports?limit=200"
        while url:
            data = requests.get(url, headers=self.headers).json()
            airports.update({i['city_name']: i['iata_city_code'] for i in data['data']})
            url = data['meta'].get('after') and f"{url}&after={data['meta']['after']}"

        return {part.strip(): iata_code for city_name, iata_code in airports.items()
                for part in (city_name.split('/') if city_name and '/' in city_name else [city_name])}

    def local_save(self):
        with open("Airports.txt", "w") as file:
            json.dump(self.airports, file, indent=4)

    def get_prices(self, slices):
        url = "https://api.duffel.com/air/offer_requests"
        passengers = [
            {"type": "adult"},
            {"type": "adult"},
            {"age": 1}
        ]

        payload = {
            "data":
                {
                    "slices": slices,
                    "passengers": passengers,
                    "cabin_class": "business",
                 }
        }

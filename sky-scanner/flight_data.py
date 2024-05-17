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
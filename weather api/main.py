import requests

f_url = "https://api.openweathermap.org/data/2.5/forecast"
key = "2dc53a7307cfc41542c6d7ee149144cd"

weather_params = {
    "lat":25.572491,
    "lon":91.310760,
    "appid": key,
    "cnt": 4
}

resp = requests.get(f_url, params=weather_params)
resp.raise_for_status()
data = resp.json()

will_rain = False
# print(data["list"][0]["weather"][0]["id"])

for hourdata in data["list"]:
    condition = hourdata["weather"][0]["id"]
    if condition<=700:
        will_rain = True

if will_rain:
    print("Bring umbrella")
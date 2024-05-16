import json
import requests

headers = {"Authorization": f"Bearer x", "Duffel-Version": "v1"}
airports = {}
url = "https://api.duffel.com/air/airports?limit=200"

while url:
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data['data'])
    airports.update({i['city_name']: i['iata_city_code'] for i in response.json()['data']})
    url = data['meta'].get('after') and f"{url}&after={data['meta']['after']}"

a2 = {}
for city_name, iata_code in airports.items():
    if "/" in city_name and city_name is not None:
        for part in city_name.split('/'):
            a2[part.strip()] = iata_code
airports.update(a2)

with open("Airports.txt", "w") as file:
    json.dump(airports, file, indent=4)

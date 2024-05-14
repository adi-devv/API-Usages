import requests
from datetime import datetime
from pprint import pprint

sheet_ep = "x"
h2 = {
    "Authorization": "Bearer huihuihui"
}

sheet_resp = requests.get(sheet_ep, headers=h2)
sheet_data = sheet_resp.json()["prices"]

flight_data = {}

if sheet_data[0]['iataCode'] == '':
    for city in sheet_data:
        city['iataCode'] = flight_data.get(city.get('name'), 'Testing')
        print(sheet_data)
        resp = requests.put(
            url=f"{sheet_ep}/{city['id']}",
            json={
                "price": {"iataCode": city["iataCode"]}
            },
            headers=h2
        )
        print(resp.text)


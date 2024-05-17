import requests, json
from flight_data import FlightData

x
sheet_ep = "https://api.sheety.co/x/flightDeals/prices"
h2 = {
    "Authorization": "Bearer x"
}

sheet_resp = requests.get(sheet_ep, headers=h2)
sheet_data = sheet_resp.json()["prices"]

file = open("Airports.txt", "r+")
airports = json.load(file)

print('runnning')

for v in sheet_data:
    if v['iataCode'] == '':
        v['iataCode'] = airports.get(v['city'], 'Missing')
        resp = requests.put(
            url=f"{sheet_ep}/{v['id']}",
            json={
                "price": {"iataCode": v["iataCode"]}
            },
            headers=h2
        )
        print(resp.text)

for v in sheet_data:
    slices = [
        {
            "origin": "BHO",
            "destination": v['iataCode'],
            "departure_date": "2024-06-21"
        },
        {
            "origin": v['iataCode'],
            "destination": "BHO",
            "departure_date": "2024-07-21"
        }
    ]
    print('a')

    v['lowestPrice'] = F.get_prices(slices)

    resp = requests.put(
        url=f"{sheet_ep}/{v['id']}",
        json={
            "price": {"lowestPrice": v["lowestPrice"]}
        },
        headers=h2
    )
    print(resp.json())
    break

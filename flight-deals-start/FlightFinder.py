import requests, json

sheet_ep = "https://api.sheety.co/x/flightDeals/prices"
h2 = {
    "Authorization": "Bearer x"
}

sheet_resp = requests.get(sheet_ep, headers=h2)
sheet_data = sheet_resp.json()["prices"]

file = open("Airports.txt","r+")
airports = json.load(file)

if sheet_data[0]['iataCode']:
    for v in sheet_data:
        v['iataCode'] = airports.get(v['city'], 'Missing')
        resp = requests.put(
            url=f"{sheet_ep}/{v['id']}",
            json={
                "price": {"iataCode": v["iataCode"]}
            },
            headers=h2
        )
        print(resp.text)
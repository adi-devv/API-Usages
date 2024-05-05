import os

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

f_url = "https://api.openweathermap.org/data/2.5/forecast"
key = "key"
acc_sid = os.environ.get("accsid")
auth_token = os.environ.get("autht")

weather_params = {
    "lat": 25.572491,
    "lon": 91.310760,
    "appid": key,
    "cnt": 4
}

resp = requests.get(f_url, params=weather_params)
resp.raise_for_status()
data = resp.json()

will_rain = False

for hourdata in data["list"]:
    condition = hourdata["weather"][0]["id"]
    if condition <= 700:
        will_rain = True

if will_rain:
    proxyClient = TwilioHttpClient()
    proxyClient.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(acc_sid, auth_token, http_client=proxyClient)
    msg = client.messages \
        .create(
            body="Gonna rain!",
            from_="+sendernum",
            to="+num"
        )

print(msg.status)

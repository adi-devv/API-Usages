import requests
from datetime import datetime

pix_ep = "https://pixe.la/v1/users"
token = "svk24iunfwnad"
usn = "aaddit"
gID = "graph1"
user_params = {
    "token": token,
    "username": usn,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# resp = requests.post(url = pix_ep, json=user_params)
# print(resp.text)

graph_ep = f"{pix_ep}/{usn}/graphs"
graph_config = {
    "id": gID,
    "name": "WalkingGraph",
    "unit": "Steps",
    "type": "float",
    "color": "sora",

}

headers = {
    "X-USER-TOKEN": token
}

# resp = requests.post(url=graph_ep, json=graph_config, headers=headers)
# print(resp.text)

pix_epp = f"{pix_ep}/{usn}/graphs/{gID}"
today = datetime.now()

pix_data = {
    "date": input("Date in YYYYMMDD format?\n"),#today.strftime("%Y%m%d"),
    "quantity": input("How many steps buddy?\n"),
}

resp = requests.post(url=pix_epp, json=pix_data, headers=headers)
print(resp.text)


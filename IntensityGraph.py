import requests

pix_ep = "https://pixe.la/v1/users"
token = "x"
usn = "x"

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
    "id": "graph1",
    "name": "WalkingGraph",
    "unit": "Steps",
    "type": "int",
    "color": "sora",

}

headers = {
    "X-USER-TOKEN": token
}

resp = requests.post(url=graph_ep, json=graph_config, headers=headers)
print(resp.text)

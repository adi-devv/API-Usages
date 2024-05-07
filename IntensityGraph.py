import requests

pix_ep = "https://pixe.la/v1/users"
token = "x"
usn = "x"

user_params = {
    "token": token ,
    "username": usn,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#resp = requests.post(url = pix_ep, json=user_params)
# print(resp.text)

graph_ep = f"{pix_ep}/{usn}"
graph_config = {
    "id": "graph1",
    "name": "WalkingGraph",
    "unit": "Steps",
    "type": "int",
    "color": "sora",

}

resp = requests.post(url = graph_ep, json = graph_config)
print(resp.text)

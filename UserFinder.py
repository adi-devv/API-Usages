import requests

user_id = #######
url = f"https://api.github.com/user/{user_id}"

response = requests.get(url, headers={"Accept": "application/vnd.github.v3+json"})
if response.status_code == 200:
    user_data = response.json()
    print(f"The GitHub profile URL for user ID {user_id} is: {user_data['html_url']}")
else:
    print(f"Failed to fetch user data: {response.status_code}")

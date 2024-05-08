import requests
from datetime import datetime

app_id = "x"
key = "x"

exercise_ep = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_ep = "https://api.sheety.co/x/myWorkouts/workouts"

headers = {
    "x-app-id": app_id,
    "x-app-key": key,
}

ex_params = {
    "query": input("Which exercise did you do?\n"),
    "gender": "M",
    "weight_kg": 50,
    "height_cm": 175,
    "age": 19,
}

resp = requests.post(exercise_ep, json=ex_params, headers=headers)
result = resp.json()
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

date = datetime.today().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

h2 = {
    "Authorization": "Bearer z"
}
for ex in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": now,
            "exercise": ex['name'].title(),
            "duration": ex['duration_min'],
            "calories": ex['nf_calories']
        }
    }

    sheet_resp = requests.post(sheet_ep, json=sheet_inputs, headers=h2)
    print(sheet_resp.text)

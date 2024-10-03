import requests
import datetime

#sheetlyBearerToken
#wy335o6G3q434%9i3h

APP_ID = "50e33904"
API_KEY = "3d60109309539bed4c2f97b699855eb6"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

sheetly_headers = {
    "Authorization": "Bearer wy335o6G3q434%9i3h"
}

sheetly_endpoint = "https://api.sheety.co/483f18e341684925174b9162ac2d8d6b/day38MyPyhtonWorkouts/workouts"

workout_input = {
    "query" : input("Which exercises did you do today? "),
    "gender" : "female",
    "weight_kg" : 47.1,
    "height_cm" : 152,
    "age": 18
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=workout_input, headers=nutritionix_headers)
workouts_json = nutritionix_response.json()

workouts_items = len(workouts_json['exercises'])
for i in range(0, workouts_items):
    workout_exercise = workouts_json['exercises'][i]['name']
    workout_duration = workouts_json['exercises'][i]['duration_min']
    workout_calories = workouts_json['exercises'][i]['nf_calories']

    today = datetime.datetime.now()
    workout_date = today.strftime("%d/%m/%Y")
    workout_time = today.strftime("%H:%M:%S")

    new_data = {
        "workout": {
            "date": workout_date,
            "time": workout_time,
            "exercise": workout_exercise.capitalize(),
            "duration": workout_duration,
            "calories": workout_calories,
        }
    }

    print(new_data)

    sheetly_response = requests.post(url=sheetly_endpoint, json=new_data, headers=sheetly_headers)
    print(f"sheetly_response.text =\n{sheetly_response.text}")
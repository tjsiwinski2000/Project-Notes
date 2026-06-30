import requests
#contants for using nutrition API
APP_ID = 'app_ad9aa21d835d453bbd5800e6'
APP_KEY = 'nix_live_1az6RnPJ9fZu2kLazV1dOS62AkUzflJT'

BASE_URL = 'https://app.100daysofpython.dev'
POST_ADDITION = '/v1/nutrition/natural/exercise'

ENDPOINT = BASE_URL + POST_ADDITION
graph_config ={
    "query": "swam for 1 hour"
}

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : APP_KEY,
}
#Create a graph
response = requests.post(url=ENDPOINT, json=graph_config, headers = headers)
print(response.text)

#Sheety Get URL
#https://api.sheety.co/15681fe5fd7a942abf74a1b88c9b690b/copyOfMyWorkouts/workouts
#Sheety POST URL
SHEETY_POST_ENDPOINT = 'https://api.sheety.co/15681fe5fd7a942abf74a1b88c9b690b/copyOfMyWorkouts/workouts'

new_sheety_entry ={
    	"workout" : {"date": "12/14/2025",
    	"time": "30:00",
        "exercise": "Bike ERG",
        "duration" : 40,
        "calories" : 200}
}

sheety_headers = {
    "Content-Type": "application/json"
}

response = requests.post(url=SHEETY_POST_ENDPOINT, json=new_sheety_entry, headers = sheety_headers )
response.raise_for_status()
print(response.text)
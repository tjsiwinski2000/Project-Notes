import requests
from datetime import datetime

MY_LAT = 29.602400
MY_LONG = -98.393089
# response = requests.get("http://api.open-notify.org/iss-now.json")
#
# data=response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG
# }
# response = requests.get(url="https://sunrise-sunset.org/api", params=parameters)
# response.raise_for_status()
# data = response
# print(type(data))
# print(data.status_code)
# print(data.content)
#1127-2025 6:00pm not returning JSON returns HTML
tj_url = "https://api.sunrise-sunset.org/json?lat=lat-me&lng=lng-me&formatted=0&tzid=America/Chicago"
tj_url=tj_url.replace("lat-me", str(MY_LAT)).replace("lng-me",str(MY_LONG))
print(tj_url)
response = requests.get(tj_url)
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset =  data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunrise)

time_now = datetime.now()
print(time_now.hour)
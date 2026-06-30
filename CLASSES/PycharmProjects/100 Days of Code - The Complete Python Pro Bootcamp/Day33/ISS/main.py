import requests
from datetime import datetime
import time

MY_LAT = 29.602400
MY_LONG = -98.393089

def space_station_near_me(me_lat, me_long, iss_lat, iss_long):
    print(f"ME: {me_lat},{me_long} ISS: {iss_lat},{iss_long}")
    latitude_difference = me_lat - iss_lat
    print(f"latitude difference: {latitude_difference}")
    longitude_difference = me_long - iss_long
    print(f"longitude difference: {longitude_difference}")
    if abs(latitude_difference) <= 5 and abs(longitude_difference) <= 5:
        return True
    else:
        return False

def is_night(sunrise_hr, sunset_hr, now_hr):
    if now_hr > sunrise_hr and now_hr < sunrise_hr:
        return  True
    else:
        return  False


while True:

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid" : "America/Chicago"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(f"sunrise hour:{sunrise}")
    print(f"sunset hour:{sunset}")

    time_now = datetime.now()
    print(f"time now hour: {time_now.hour}")
    # BONUS: run the code every 60 seconds.

    if space_station_near_me(MY_LAT, MY_LONG, iss_latitude, iss_longitude):
        if is_night(sunrise,sunset,time_now.hour):
            print("send e-mail")
    else:
        print("Alas the ISS is not overhead at this time.")

    print("Starting sleep cycle")
    time.sleep(15)
    print("Sleep finished")
#consider creating a function that returns true if your position is within plus five



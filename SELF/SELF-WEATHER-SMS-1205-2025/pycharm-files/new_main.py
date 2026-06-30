import requests
import time
from new_weather_codes import OPENWEATHER_CODES
#Note to find rainy city ->https://www.ventusky.com and -> https://www.latlong.net/

# San Antonio , Texas
MY_LAT = 29.602400
MY_LONG = -98.393089
# Brooklyn, NY
# MY_LAT = 40.678177
# MY_LONG = -73.944160
# Suwon ,SK
# MY_LAT = 37.28
# MY_LONG = 127.01


api_key = "d9d63ca3b4ff15ad9ad44471ee221661"
url_weather="https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : api_key,
    "cnt" : 4,
    "units" : "imperial"
}

response = requests.get(url=url_weather, params=parameters)
response.raise_for_status()
data = response.json()
#SAVE DEBUG print(data)

report=[]
timestr = time.strftime("%H:%M")
for forecast_num in range(0,4):
    weather_code = data["list"][forecast_num]["weather"][0]["id"]
    temp=round(data["list"][forecast_num]["main"]["temp"])
    icon = OPENWEATHER_CODES[weather_code]['icon']
    description = OPENWEATHER_CODES[weather_code]['description']
    #SAVE DEBUG print(f"forecast_num: {forecast_num} , weather_code: {weather_code}, {OPENWEATHER_CODES[weather_code]['main']}, {OPENWEATHER_CODES[weather_code]['description']}")
    if forecast_num == 0:
        report.append(f"Weather at {timestr}")
        report.append(f"-{icon}  {temp}° Fahrenheit  with {description}")
    else:
        hour = forecast_num *3
        report.append(f"In {hour} hrs expect")
        report.append(f"-{icon}  {temp}° Fahrenheit  with {description}")


for line in report:
    print(line)


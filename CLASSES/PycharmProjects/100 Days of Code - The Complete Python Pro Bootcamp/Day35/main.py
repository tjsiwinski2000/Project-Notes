import requests
import time
import os
from weather_codes import OPENWEATHER_CODES
#Note to find rainy city ->https://www.ventusky.com and -> https://www.latlong.net/
# -11.831310, -61.319698 Randonia 1203-2025 python bootcamp udemy

# San Antonio , Texas
MY_LAT = 29.602400
MY_LONG = -98.393089
# Brooklyn, NY
MY_LAT = 40.678177
MY_LONG = -73.944160
# Suwon ,SK
# MY_LAT = 37.28
# MY_LONG = 127.01


api_key = os.environ.get('WEATHER_API_KEY')

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
print(data)

# determine calls to get weather next 9 hours
# develop weather report string
# text weather report string to CORY
# python anywhere and schedule

# bring_umbrella = False
report=""
timestr = time.strftime("%H:%M")
for forecast_num in range(0,4):
    weather_code = data["list"][forecast_num]["weather"][0]["id"]
    temp=round(data["list"][forecast_num]["main"]["temp"])
    print(f"forecast_num: {forecast_num} , weather_code: {weather_code}, {OPENWEATHER_CODES[weather_code]['main']}, {OPENWEATHER_CODES[weather_code]['description']}")
    if forecast_num == 0:
        report += f"Weather at {timestr} temp is: {temp} {OPENWEATHER_CODES[weather_code]['main']}, {OPENWEATHER_CODES[weather_code]['description']}"
    else:
        hour = forecast_num *3
        report += f"\nin {hour} hrs expect temp:{temp} with {OPENWEATHER_CODES[weather_code]['main']}, {OPENWEATHER_CODES[weather_code]['description']}"

#print(f"Bring Umbrella: {bring_umbrella}")
#print(report)

send_text = True
if send_text:
    resp = requests.post('https://textbelt.com/text', {
      'phone': '2107896843',
      'message': f'from TJ-> SA weather: {report}',
      'key': 'aff78de27e57501288e30b4255d3b43219eaee57gpEDSvZbIlwriJIB4W63DIwjQ',
    })
    print(resp.json())

print(report)

# with open("weather-data.txt","w") as f1:
#     f1.write((str(data)))
#
# for key in data.keys():
#     print(f"{key} : {data[key]}")
#
# print(data["list"][0]['main']['temp_max'])
# data_list = data["list"]
# print(type(data_list))
# list_main= data_list[0]
# print(type(list_main))
# dict_main= list_main['main']
# print(dict_main['temp_max'])
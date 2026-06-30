import requests
import time
from new_weather_codes import OPENWEATHER_CODES

# San Antonio, Texas
MY_LAT = 29.602400
MY_LONG = -98.393089

api_key = "d9d63ca3b4ff15ad9ad44471ee221661"
url_weather = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
    "units": "imperial"
}

response = requests.get(url=url_weather, params=parameters)
response.raise_for_status()
data = response.json()

report = []
current_time = time.strftime("%H:%M")

for i in range(4):
    
    forecast = data["list"][i]
    weather_id = forecast["weather"][0]["id"]
    temp = round(forecast["main"]["temp"])
    
    # Get info from your dict with a safe fallback
    weather_info = OPENWEATHER_CODES.get(weather_id, {"icon": "❓", "description": "unknown"})
    icon = weather_info['icon']
    desc = weather_info['description']

    if i == 0:
        temperature_text = f"Weather at {current_time} temp is: {temp} with"
    else:
        hours = i * 3
        temperature_text = f"in {hours} hrs expect temp: {temp} with"
    my_dict ={
        "temperature":temperature_text,
        "icon":icon,
        "description":desc
    }
    report.append(my_dict)
    # if i == 0:
    #     report.append(f"Weather at {current_time}")
    #     report.append(f"-{icon}  {temp}° Fahrenheit  with {desc}")
    # else:
    #     hour = i *3
    #     report.append(f"In {hour} hrs expect")
    #     report.append(f"-{icon}  {temp}° Fahrenheit  with {desc}")

# Print the final report
for line in report:
    print(line)
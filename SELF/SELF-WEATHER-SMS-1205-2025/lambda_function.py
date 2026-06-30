import json
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

def lambda_handler(event, context):
    OPENWEATHER_CODES = {
    # Thunderstorm 200–232
    200: {"main": "Thunderstorm", "description": "thunderstorm with light rain"},
    201: {"main": "Thunderstorm", "description": "thunderstorm with rain"},
    202: {"main": "Thunderstorm", "description": "thunderstorm with heavy rain"},
    210: {"main": "Thunderstorm", "description": "light thunderstorm"},
    211: {"main": "Thunderstorm", "description": "thunderstorm"},
    212: {"main": "Thunderstorm", "description": "heavy thunderstorm"},
    221: {"main": "Thunderstorm", "description": "ragged thunderstorm"},
    230: {"main": "Thunderstorm", "description": "thunderstorm with light drizzle"},
    231: {"main": "Thunderstorm", "description": "thunderstorm with drizzle"},
    232: {"main": "Thunderstorm", "description": "thunderstorm with heavy drizzle"},

    # Drizzle 300–321
    300: {"main": "Drizzle", "description": "light intensity drizzle"},
    301: {"main": "Drizzle", "description": "drizzle"},
    302: {"main": "Drizzle", "description": "heavy intensity drizzle"},
    310: {"main": "Drizzle", "description": "light intensity drizzle rain"},
    311: {"main": "Drizzle", "description": "drizzle rain"},
    312: {"main": "Drizzle", "description": "heavy intensity drizzle rain"},
    313: {"main": "Drizzle", "description": "shower rain and drizzle"},
    314: {"main": "Drizzle", "description": "heavy shower rain and drizzle"},
    321: {"main": "Drizzle", "description": "shower drizzle"},

    # Rain 500–531
    500: {"main": "Rain", "description": "light rain"},
    501: {"main": "Rain", "description": "moderate rain"},
    502: {"main": "Rain", "description": "heavy intensity rain"},
    503: {"main": "Rain", "description": "very heavy rain"},
    504: {"main": "Rain", "description": "extreme rain"},
    511: {"main": "Rain", "description": "freezing rain"},
    520: {"main": "Rain", "description": "light intensity shower rain"},
    521: {"main": "Rain", "description": "shower rain"},
    522: {"main": "Rain", "description": "heavy intensity shower rain"},
    531: {"main": "Rain", "description": "ragged shower rain"},

    # Snow 600–622
    600: {"main": "Snow", "description": "light snow"},
    601: {"main": "Snow", "description": "snow"},
    602: {"main": "Snow", "description": "heavy snow"},
    611: {"main": "Snow", "description": "sleet"},
    612: {"main": "Snow", "description": "light shower sleet"},
    613: {"main": "Snow", "description": "shower sleet"},
    615: {"main": "Snow", "description": "light rain and snow"},
    616: {"main": "Snow", "description": "rain and snow"},
    620: {"main": "Snow", "description": "light shower snow"},
    621: {"main": "Snow", "description": "shower snow"},
    622: {"main": "Snow", "description": "heavy shower snow"},

    # Atmosphere 701–781
    701: {"main": "Mist", "description": "mist"},
    711: {"main": "Smoke", "description": "smoke"},
    721: {"main": "Haze", "description": "haze"},
    731: {"main": "Dust", "description": "sand/dust whirls"},
    741: {"main": "Fog", "description": "fog"},
    751: {"main": "Sand", "description": "sand"},
    761: {"main": "Dust", "description": "dust"},
    762: {"main": "Ash", "description": "volcanic ash"},
    771: {"main": "Squall", "description": "squalls"},
    781: {"main": "Tornado", "description": "tornado"},

    # Clear 800
    800: {"main": "Clear", "description": "clear sky"},

    # Clouds 801–804
    801: {"main": "Clouds", "description": "few clouds"},
    802: {"main": "Clouds", "description": "scattered clouds"},
    803: {"main": "Clouds", "description": "broken clouds"},
    804: {"main": "Clouds", "description": "overcast clouds"},
    }
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

    report=""
    utc_now = datetime.now(ZoneInfo("UTC"))
    cst_timezone = ZoneInfo("America/Chicago")  # Or "US/Central"
    cst_now = utc_now.astimezone(cst_timezone)
    
    timestr = cst_now.strftime("%H:%M")
    for forecast_num in range(0,4):
        weather_code = data["list"][forecast_num]["weather"][0]["id"]
        temp=round(data["list"][forecast_num]["main"]["temp"])
        print(f"forecast_num: {forecast_num} , weather_code: {weather_code}, {OPENWEATHER_CODES[weather_code]['main']}, {OPENWEATHER_CODES[weather_code]['description']}")
        if forecast_num == 0:
            report += f"Weather at {timestr} temp is: {temp} {OPENWEATHER_CODES[weather_code]['main']}, {OPENWEATHER_CODES[weather_code]['description']}"
        else:
            hour = forecast_num *3
            report += f"--in {hour} hrs expect temp:{temp} with {OPENWEATHER_CODES[weather_code]['main']}, {OPENWEATHER_CODES[weather_code]['description']}"
    
    resp = requests.post('https://textbelt.com/text', {
      'phone': '2107896843',
      'message': f'TJ: SA weather: {report}',
      'key': 'aff78de27e57501288e30b4255d3b43219eaee57gpEDSvZbIlwriJIB4W63DIwjQ',
    })
    print(resp.json())
    return {
        'statusCode': 200,
        'body': json.dumps(resp.json())
    }

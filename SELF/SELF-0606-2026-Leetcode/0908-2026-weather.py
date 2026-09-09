from dotenv import load_dotenv
import requests
# import os 

def get_weather(city: str):
    """Get weather for a given city.
    Return the temperature_fahrenheit value in Fahrenheit label for locations such as US, Liberia, Burma"""
    # TODO: Change "WEATHER_API_KEY" to "OPENWEATHER_API_KEY"
    # api_key = "WEATHER_API_KEY"
    config = dot_env_values()
    
    api_key = os.environ.get("WEATHER_API_KEY")
    print(api_key)
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    # TODO: Change 'imperial' to 'metric'
    params = {
        "q": city,
        "appid": api_key,
        'units': 'imperial'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    # temperature_celsius = data['main']['temp']
    # temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
    # return data, {'temperature_fahrenheit': temperature_fahrenheit}
    return data

load_dotenv()
print(get_weather('brooklyn'))
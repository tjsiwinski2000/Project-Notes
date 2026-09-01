# Fix the Real Weather API Call

This script is a weather assistant agent that fetches live weather data from the OpenWeatherMap API. The `get_weather` function makes a real HTTP request to the API using an API key stored in the `.env` file, and returns the temperature and conditions for any city.

The starter code has two mistakes in `get_weather`. Fix them:

1. The environment variable name is wrong. Change `"WEATHER_API_KEY"` to `"OPENWEATHER_API_KEY"`.
2. The units parameter is wrong. Change `'units': 'imperial'` to `'units': 'metric'`.

Everything else is correct.

**Important:** You need an OpenWeatherMap API key to run this code. Sign up for free at [openweathermap.org](https://openweathermap.org/api), then add your key to the `.env` file alongside your Google API key.

<div class="hint">

`os.getenv("OPENWEATHER_API_KEY")` reads the value from your `.env` file.

</div>

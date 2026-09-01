# Complete get_location()

This script is a weather assistant agent that automatically detects the user's city by making a request to a free IP geolocation API. The `get_location` function queries `ipapi.co`, which returns location data based on the caller's IP address, and returns a formatted city and country string that the agent can use.

Complete the body of `get_location()` so that it:

1. Makes a GET request to `"https://ipapi.co/json/"` with the header `{'User-agent': 'your-bot 0.1'}`.
2. Parses the JSON response to extract `'city'` and `'country_name'`.
3. Returns the result as an f-string: `f"{city}, {country}"`.

**Important:** Make sure your `.env` file has your Google API key before running the code.

<div class="hint">

Use `requests.get(url, headers=...)` and call `.json()` on the response to parse it.

</div>

<div class="hint">

The keys in the response JSON are `'city'` and `'country_name'`. Store `'country_name'` using `.get('country_name')`.

</div>

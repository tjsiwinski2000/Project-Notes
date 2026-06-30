#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests

def get_access_token():
    ENDPOINT_AMADEUS_ACCESS_TOKEN="https://test.api.amadeus.com/v1/security/oauth2/token"

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    APIKEY='2f59gc7FbP96F2F5NqUwYyy06GteUZv6'
    APISecret ='YY9PGsMs3Oc7r8Zj'
    client_credentials='client_credentials'
    body =f"grant_type={client_credentials}&client_id={APIKEY}&client_secret={APISecret}"
    response = requests.post(url=ENDPOINT_AMADEUS_ACCESS_TOKEN, data=body, headers = headers)
    print(response.text)

get_access_token()

# 1218-2025 955am
# {
#     "type": "amadeusOAuth2Token",
#     "username": "tjsiwinski_2000@yahoo.com",
#     "application_name": "NYC2026",
#     "client_id": "2f59gc7FbP96F2F5NqUwYyy06GteUZv6",
#     "token_type": "Bearer",
#     "access_token": "xBiex0QAse3RdpOHasr3HRRsT6ti",
#     "expires_in": 1799,
#     "state": "approved",
#     "scope": ""
# # }

import json


def search_flights_to_nyc(access_token):
    # API Endpoint for Flight Offers Search (v2 is the current stable version)
    url = "https://test.api.amadeus.com/v2/shopping/flight-offers"

    # Your Bearer token must be in the Authorization header
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Parameters for the search
    params = {
        "originLocationCode": "SAT",  # Departure City (e.g., London)
        "destinationLocationCode": "NYC",  # Arrival City (New York - covers JFK, LGA, EWR)
        "departureDate": "2026-01-15",  # Date in YYYY-MM-DD format
        "returnDate": "2026-01-20",
        "adults": 2,  # Number of adult passengers
        "currencyCode": "USD",
        "max": 5  # Limit results to top 5 offers
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        print(response.text)
        print("*" *50)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print(f"Found {len(data['data'])} flight offers!")

            # Print the first flight price as an example
            if data['data']:
                first_offer = data['data'][0]
                price = first_offer['price']['total']
                currency = first_offer['price']['currency']
                print(f"The cheapest flight found is {price} {currency}")

            return data
        else:
            print(f"Error: {response.status_code}")
            print(response.json())
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Use your actual token here
MY_TOKEN = "xBiex0QAse3RdpOHasr3HRRsT6ti"
#results = search_flights_to_nyc(MY_TOKEN)
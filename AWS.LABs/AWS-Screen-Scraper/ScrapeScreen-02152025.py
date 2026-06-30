import json
import requests
#import beautifulsoup4 
from bs4 import BeautifulSoup

def lambda_handler():
    url = "https://cnn.com"  # The website you want to scrape
    print("Hello from a function")
    # Fetch the content of the URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Will raise an exception for 4xx/5xx responses
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error fetching page: {str(e)}")
        }

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract information from the page (e.g., all links in the page)
    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])

    # Return the links in a JSON response
    return {
        'statusCode': 200,
        'body': json.dumps({
            'links': links
        })
    }

    lambda_handler("a" , "b")
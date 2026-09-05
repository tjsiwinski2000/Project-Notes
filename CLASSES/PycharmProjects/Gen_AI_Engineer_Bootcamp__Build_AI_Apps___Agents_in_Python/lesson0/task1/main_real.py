# Welcome to the AI Developer Bootcamp!
# There is nothing to run here — read the instructions in the Task Description panel on the right.
# Once you have set up your API keys, click Next Task to begin coding.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
#
from langchain.agents import create_agent
import os
import requests

# from lesson2.task1.task import get_location

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

# determine what's available
# from  google import genai
# client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
#
# for m in client.models.list():
#     if 'lite' in m.name.lower():
#         print(m.name)

# load_dotenv()
def get_weather(city:str):
    """Get Weather for a given city"""
    api_key = os.environ.get('WEATHER_API_KEY')
    base_url= "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q" : city,
        "appid" : api_key,
        'units' :'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_location():
    """Get user's location. Use this when the user asks about the weather without specifying a city"""
    response = requests.get("https://ipapi.co/json/", headers = {'User-agent': 'your-bot 0.1'})
    data = response.json()
    city = data['city']
    country = data.get('country_name')
    return f"{city}, {country}"

llm = ChatGoogleGenerativeAI(
    model = 'gemini-flash-lite-latest',
    temperature = 0.7,
    max_output_tokens=256,  # cap it
)

# response1= llm.invoke("how is the weather in Rome?")
# print(response1.content)

system_prompt= """
You are a helpful weather assistant
YOUR WORKFLOW:
1. if the user asks about weather WITHOUT specifying a location you MUST:
-  first call get location to find their location 
- then call get_weather(city) with that location

2. If the user provides a city call get_weather(city) directly.
"""
agent = create_agent(
    model=llm,
    tools = [get_weather,get_location],
    system_prompt=system_prompt
)
#
if __name__ == "__main__":
    user_query = input("Enter your query: ")
    # response1 = llm.invoke("How is the weather in Rome?")
    response1 = agent.invoke(
        {"messages": ({'role': 'user',
                       'content': user_query})})
    print(response1['messages'][-1].content)
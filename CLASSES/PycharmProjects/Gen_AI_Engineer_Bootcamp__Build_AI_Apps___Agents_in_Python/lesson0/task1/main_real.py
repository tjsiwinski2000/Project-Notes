# Welcome to the AI Developer Bootcamp!
# There is nothing to run here — read the instructions in the Task Description panel on the right.
# Once you have set up your API keys, click Next Task to begin coding.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
#
from langchain.agents import create_agent
# from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import  SqliteSaver

import os
import requests

# from lesson4.task1.task import checkpointer

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
    """Get Weather for a given city.
    Return temperature in Fahrenheit for locations such as US, Liberia, Burma"""
    api_key = os.environ.get('WEATHER_API_KEY')
    base_url= "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q" : city,
        "appid" : api_key,
        'units' :'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    temperature_celsius = data['main']['temp']
    temperature_fahrenheit = temperature_celsius *9/5 +32
    f= {'temperature_fahrenheit': temperature_fahrenheit}
    return data, f

def get_location():
    """Get user's location. Use this when the user asks about the weather without specifying a city"""
    response = requests.get("https://ipapi.co/json/", headers = {'User-agent': 'your-bot 0.1'})
    data = response.json()
    city = data['city']
    country = data.get('country_name')
    return f"{city}, {country}"

llm = ChatGoogleGenerativeAI(
    # model = 'gemini-flash-lite-latest',
    model = 'gemini-3.1-flash-lite',
    temperature = 0.7,
    max_output_tokens=512,  # cap it
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

3. Use your knowledge to determine which temperature unit is standard for the given location.

4. Present the weather information including temperature, condition, wind speed, and any other relevant details.
"""

with SqliteSaver.from_conn_string('checkpoints.db') as checkpointer :
    agent = create_agent(
        model=llm,
        tools = [get_weather,get_location],
        system_prompt=system_prompt,
        checkpointer=checkpointer,
    )
    #

    while True:
        user_query = input("Enter your query: ")
        # response1 = llm.invoke("How is the weather in Rome?")
        if user_query in ('bye','quit', 'exit'):
            break
        response = agent.invoke(
            {"messages": ({'role': 'user',
                           'content': user_query})},
            {"configurable": {"thread_id":"1"}})
        print(f'testing get_location: {get_location()}')
        print(response['messages'][-1].content)





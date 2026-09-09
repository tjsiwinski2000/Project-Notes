from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.checkpoint.postgres import PostgresSaver
import requests
import os
load_dotenv()

DB_URI = "postgresql://postgres.ipxasoyjgndlogkplfsi:AIfofoo%401965@aws-0-us-east-1.pooler.supabase.com:6543/postgres"

def get_weather(city: str):
    """Get weather for a given city.
    Return the temperature_fahrenheit value in Fahrenheit label for locations such as US, Liberia, Burma"""
    # TODO: Change "WEATHER_API_KEY" to "OPENWEATHER_API_KEY"
    api_key = os.environ.get("WEATHER_API_KEY")
    # print(api_key)
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    # TODO: Change 'imperial' to 'metric'
    params = {
        "q": city,
        "appid": api_key,
        'units': 'imperial'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    temperature_celsius = data['main']['temp']
    temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
    # return data, {'temperature_fahrenheit': temperature_fahrenheit}
    return data


def get_location():
    """Get user's current location. Use this when the user asks about weather."""
    response = requests.get("https://ipapi.co/json/", headers={'User-agent': 'your-bot 0.1'})
    data = response.json()
    city = data['city']
    country = data.get('country_name')
    return f"{city}, {country}"


llm = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    temperature=0.7,
)

system_prompt = """
You are a helpful weather assistant.
YOUR WORKFLOW:
1. If the user asks about weather WITHOUT specifying a location, you MUST:
   - First call get_location() to find their location
   - Then call get_weather(city) with that location

2. If the user provides a city, call get_weather(city) directly.
"""

with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
    checkpointer.setup()
    agent = create_agent(
        model=llm,
        tools=[get_weather, get_location],
        system_prompt=system_prompt,
        checkpointer=checkpointer
    )

    while True:
        user_query = input("Enter your query: ")
        if user_query.strip() in ['bye', 'quit', 'exit']:
            break
        response = agent.invoke(
            {"messages": [{'role': 'user', 'content': user_query}]},
            {"configurable": {"thread_id": "1"}}
        )

        # TODO: loop over response['messages']; print 'You: ' + content for human messages, 'Agent: ' + content for ai messages with non-empty content

        #print(response['messages'][-1].content)
        # for i in response['messages']:
        #     if i.type == 'human':
        #         print("You ", i.content)
        #     if i.type == 'ai' and i.content:
        #         print("Agent: ", i.content)

        print(response['messages'][-1].content)

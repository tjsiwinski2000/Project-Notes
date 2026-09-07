# 0907-2026 - reviewed 8:20am
# This is working w/o issue.
# INTRODUCTION to Agents

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_agent

# import os
# GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
# GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

# load env. variables
load_dotenv()


def get_weather(city: str):
    """Get weather for a given city"""
    return {'condition': 'sunny', 'temperature': 25}


def get_location():
    """Get user's current location. Use this when the user asks about weather."""
    return "Rome, Italy"


# NOTE : reads google API key automatically via load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-flash-lite-latest",
    temperature=0.3,
)

system_prompt = """
You are a helpful weather assistant.
YOUR WORKFLOW:
1. If the user asks about weather WITHOUT specifying a location, you MUST:
   - First call get_location() to find their location
   - Then call get_weather(city) with that location

2. If the user provides a city, call get_weather(city) directly.
"""

agent = create_agent(
    model=llm,
    tools=[get_weather, get_location],
    system_prompt=system_prompt
)

user_query = input("Enter your query: ")

response = agent.invoke(
    {"messages": [{'role': 'user', 'content': user_query}]})
print(response['messages'][-1].content)

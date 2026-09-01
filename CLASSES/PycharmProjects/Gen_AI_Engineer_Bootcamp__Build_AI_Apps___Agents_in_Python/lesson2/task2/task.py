from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


def get_weather(city: str):
    """Get weather for a given city"""
    return {'condition': 'cloudy', 'temperature': 18}


def get_location():
    """Get user's current location. Use this when the user asks about weather."""
    return "Paris, France"


llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
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

agent = create_agent(
    model=llm,
    tools=[get_weather, get_location],
    system_prompt=system_prompt
)

user_query = "What is the weather like?"

# TODO: invoke the agent with user_query as a 'user' message, then print response['messages'][-1].content

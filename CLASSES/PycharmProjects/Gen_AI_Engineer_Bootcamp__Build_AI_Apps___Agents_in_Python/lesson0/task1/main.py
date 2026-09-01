# Welcome to the AI Developer Bootcamp!
# There is nothing to run here — read the instructions in the Task Description panel on the right.
# Once you have set up your API keys, click Next Task to begin coding.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.agents import create_agent
import os

# GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

llm = ChatGoogleGenerativeAI(
    model = 'gemini-3.6-flash',
    temperature = 0.7,
)

agent = create_agent(
    model=llm
)

# response1 = llm.invoke("How is the weather in Rome?")
response1 = agent.invoke(
    {"messages": ({'role': 'user',
                   'content':'who is the greatest tennis player in history'})})
print(response1['messages'][1].content)
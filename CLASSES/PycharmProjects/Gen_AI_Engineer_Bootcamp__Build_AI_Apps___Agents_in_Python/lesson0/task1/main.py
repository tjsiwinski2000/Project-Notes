# Welcome to the AI Developer Bootcamp!
# There is nothing to run here — read the instructions in the Task Description panel on the right.
# Once you have set up your API keys, click Next Task to begin coding.

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
import os
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

model = init_chat_model(
    model = 'gemini-3.1-flash-lite',
    model_provider='google-gemini',
    api_key= GOOGLE_API_KEY
)
response = model.invoke("Hi who is best baseball of all time?")
print((response.content[0]['text']))
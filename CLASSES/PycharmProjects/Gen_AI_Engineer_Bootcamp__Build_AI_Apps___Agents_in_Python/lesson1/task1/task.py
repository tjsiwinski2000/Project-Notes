import os

from langchain.chat_models import init_chat_model
# from os import environ
import os

# GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
# TODO: Change the model name to "gemini-3-flash-preview"
model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY)

# TODO: Change the prompt to "What is artificial intelligence in one sentence?"
# response = model.invoke("What is artificial intelligence in one sentence?")
response = model.invoke("What is best place to do whale watching in the USA")
print(response.content[0]['text'])

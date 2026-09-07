from langchain.chat_models import init_chat_model

import os
# GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY)

with open('wood.txt') as f:
    coffee = f.read()

response = model.invoke(f"Tell me about {coffee}")


print(response.content[0]['text'])

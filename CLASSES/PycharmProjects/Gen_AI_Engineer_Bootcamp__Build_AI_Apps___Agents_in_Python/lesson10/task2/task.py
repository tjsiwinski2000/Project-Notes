import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def summarize_with_ai(text):
    # TODO: define a system_prompt that asks for a concise summary; init_chat_model("gemini-3-flash-preview", api_key=GEMINI_API_KEY, model_provider="google_genai"); build [{role: system, content: system_prompt}, {role: user, content: text}] as message; return model.invoke(message).content
    pass


# Test the function
sample_data = "Name, Score\nAlice, 95\nBob, 87\nCarla, 92"
result = summarize_with_ai(sample_data)
print(result)

from langchain.chat_models import init_chat_model

# TODO: Change model_provider to "ollama" and model to 'llama3.2:1b'
model = init_chat_model(
    model='llama3.2:3b',
    model_provider="openai"
)

response = model.invoke("Can I learn Python in one year?")
print(response.text)

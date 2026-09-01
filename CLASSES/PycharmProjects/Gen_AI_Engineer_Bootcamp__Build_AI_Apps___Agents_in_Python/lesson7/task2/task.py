from langchain.chat_models import init_chat_model

model = init_chat_model(
    model='llama3.2:1b',
    model_provider="ollama"
)

# TODO: invoke the model with the prompt "What is machine learning in one sentence?" and store in response, then print response.text

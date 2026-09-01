# Initialize a Chat Model

This script connects to a Google Gemini model using LangChain and asks it a question, then prints the model's answer.

Your job is to fix the two mistakes in the starter code:

1. The model name is wrong. Change it from `"gemini-1.5-flash"` to `"gemini-3-flash-preview"`.
2. The prompt is wrong. Change it to `"What is artificial intelligence in one sentence?"`.

Everything else — the import, the API key variable, the provider, and the print statement — is already correct. Do not change those.

**Important:** Replace `"YOUR_GOOGLE_API_KEY"` with your actual Google API key before running the code. Without a valid key the program will not be able to connect to the model.

<div class="hint">

`init_chat_model` accepts `model`, `model_provider`, and `api_key` as keyword arguments.

</div>

<div class="hint">

Pass the prompt string directly to `model.invoke(...)`.

</div>

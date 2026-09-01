# Set Up an Ollama Model

This script runs a locally hosted language model using Ollama — no internet connection or API key required. LangChain connects to Ollama the same way it connects to cloud models, just with a different provider and model name.

The starter code has two mistakes. Fix them:

1. The model provider is wrong. Change `"openai"` to `"ollama"`.
2. The model name is wrong. Change `'llama3.2:3b'` to `'llama3.2:1b'`.

**Note:** Ollama must be installed and running on your machine, and the `llama3.2:1b` model must be pulled (`ollama pull llama3.2:1b`) before you can run this script.

<div class="hint">

`init_chat_model` uses `model_provider` to know which service to connect to. For local Ollama models, this should be `"ollama"`.

</div>

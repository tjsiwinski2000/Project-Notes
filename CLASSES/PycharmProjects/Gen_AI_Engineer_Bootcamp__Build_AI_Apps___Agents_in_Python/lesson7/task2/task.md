# Invoke a Local Model

This script connects to a local Ollama model and asks it a question. The response is accessed via `response.text` — the same property used for locally-hosted models in LangChain.

The model is already set up. Complete the two missing lines:

1. Invoke the model with the prompt `"What is machine learning in one sentence?"` and store the result in `response`.
2. Print `response.text`.

**Note:** Ollama must be installed, running, and have the `llama3.2:1b` model pulled before you can run this script.

<div class="hint">

Call `model.invoke(...)` with your prompt string and store the result in `response`.

</div>

<div class="hint">

Access the model's answer with `response.text` — not `response.content`.

</div>

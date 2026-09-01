# Set Up the LLM for Your Agent

This script builds a weather assistant agent with two tools: one that returns the weather for a given city, and one that detects the user's current location. The agent decides on its own which tools to call based on the user's question.

The starter code has two mistakes. Fix them:

1. The model name is wrong. Change it from `"gemini-1.5-flash"` to `"gemini-3-flash-preview"`.
2. The temperature is wrong. Change it from `0.3` to `0.7`.

Everything else is correct — do not change it.

**Important:** Open the `.env` file in this task and replace the placeholder with your actual Google API key before running the code.

<div class="hint">

`ChatGoogleGenerativeAI` accepts `model` and `temperature` as keyword arguments.

</div>

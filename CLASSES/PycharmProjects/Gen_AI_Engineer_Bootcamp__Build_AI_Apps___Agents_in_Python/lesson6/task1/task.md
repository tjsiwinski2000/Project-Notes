# Fix agent.py

This project turns the weather assistant agent into a web app using Flask. The project is split across two files: `agent.py` sets up the LLM, tools, and agent; `app.py` serves the chat interface in the browser and passes user messages to the agent.

This task focuses on `agent.py`. The starter code has two mistakes. Fix them:

1. The model name is wrong. Change `"gemini-1.5-flash"` to `"gemini-3-flash-preview"`.
2. The temperature is wrong. Change `0.3` to `0.7`.

Everything else is correct.

**Important:** Make sure your `.env` file has your API keys before running the code.

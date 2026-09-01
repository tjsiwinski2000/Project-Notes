# Fix the Flask LLM Server

This script is a Flask web server that wraps a local Ollama model and exposes it as an HTTP API. Any client — including the one in the next task — can send a POST request with a conversation history and receive the model's reply as JSON.

The starter code has two mistakes. Fix them:

1. The route is wrong. Change `"/ask"` to `"/chat"`.
2. The port is wrong. Change `5001` to `5002`.

Everything else is correct.

**Note:** Ollama must be installed and running with `llama3.2:1b` pulled before you start this server.

<div class="hint">

The route decorator is `@app.route(...)`. The port is set in `app.run(...)`.

</div>

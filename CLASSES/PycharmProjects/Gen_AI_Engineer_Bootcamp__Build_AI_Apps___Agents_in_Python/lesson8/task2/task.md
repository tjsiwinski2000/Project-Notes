# Complete the Chat Client

This script is a command-line client that talks to the LLM server from the previous task. It maintains a conversation history list and sends the full history to the server on every message, which allows the model to remember what was said earlier in the conversation.

The `server.py` file is provided for reference — you do not need to edit it.

The `while True` loop structure is given. Complete the three missing steps inside the loop:

1. Append the user's message to `history` as `{"role": "user", "content": user_input}`.
2. Send a POST request to `url` with `json={"messages": history}` and store the result in `response`.
3. Extract `assistant_message` from `response.json()['message']`, append it to `history`, and print `assistant_message['content']`.

<div class="hint">

Use `requests.post(url, json=...)` to send the request.

</div>

<div class="hint">

`response.json()['message']` returns the full message dict. Print its `'content'` key.

</div>

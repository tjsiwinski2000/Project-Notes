# Complete the /send Route in app.py

This Flask web app serves a browser-based chat interface for the weather assistant agent. When a user submits a message, the `/send` route passes it to the agent, stores both the user message and the AI response in the session, then redirects back to the chat page where the full conversation is displayed.

The `agent.py` file is provided and already complete — you do not need to edit it. Complete the missing pieces inside the `send()` function in `task.py`:

1. Invoke the agent with the user's message using `session['thread_id']` as the `thread_id`. Store the result in `response`.
2. Append `{'type': 'human', 'content': user_message}` to `session['messages']`.
3. Append `{'type': 'ai', 'content': response['messages'][-1].content}` to `session['messages']`.
4. Set `session.modified = True` so Flask knows the session changed.

**Important:** Make sure your `.env` file has your API keys before running the app.

<div class="hint">

`agent.invoke({"messages": [...]}, {"configurable": {"thread_id": session['thread_id']}})` is the same pattern used in the terminal version.

</div>

<div class="hint">

`session['messages'].append({...})` adds a new message dict to the list.

</div>

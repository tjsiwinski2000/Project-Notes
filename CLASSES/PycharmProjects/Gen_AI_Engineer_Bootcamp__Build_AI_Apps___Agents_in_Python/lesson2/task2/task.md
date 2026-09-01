# Invoke the Agent

This script builds a weather assistant agent with two tools: one that returns the weather for a given city, and one that returns the user's location. When invoked, the agent uses these tools to answer the user's question and returns a response.

The agent is already set up. Your job is to complete the two missing lines that run the agent and display its answer:

1. Invoke the agent by passing a messages list to `agent.invoke(...)`. The messages list should contain one dict with `'role': 'user'` and `'content': user_query`. Store the result in a variable called `response`.
2. Print the content of the last message with `print(response['messages'][-1].content)`.

**Important:** Open the `.env` file and replace the placeholder with your actual Google API key before running the code.

<div class="hint">

`agent.invoke()` takes a dict with a `"messages"` key. Each message is a dict with `"role"` and `"content"`.

</div>

<div class="hint">

`response['messages']` is a list. Use index `-1` to get the last item, then access `.content`.

</div>

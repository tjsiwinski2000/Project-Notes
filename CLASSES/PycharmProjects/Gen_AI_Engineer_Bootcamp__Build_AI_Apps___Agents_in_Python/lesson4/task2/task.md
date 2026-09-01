# Write the Conversation Loop

This script runs a multi-turn weather assistant in the terminal. The agent remembers the full conversation history using a SQLite checkpointer, so users can ask follow-up questions naturally. The loop keeps running until the user types a quit command.

The agent and checkpointer are already set up. Write the `while True` loop inside the `with SqliteSaver...` block:

1. Get user input with `input("Enter your query: ")` and store it in `user_query`.
2. Break out of the loop if `user_query` is `'bye'`, `'quit'`, or `'exit'`.
3. Invoke the agent with the user message and `thread_id="1"` in the configurable, storing the result in `response`.
4. Print the last message with `print(response['messages'][-1].content)`.

**Important:** Make sure your `.env` file has your Google API key before running the code.

<div class="hint">

Use `if user_query in ['bye', 'quit', 'exit']: break` to exit the loop.

</div>

<div class="hint">

Pass `{"configurable": {"thread_id": "1"}}` as the second argument to `agent.invoke()`.

</div>

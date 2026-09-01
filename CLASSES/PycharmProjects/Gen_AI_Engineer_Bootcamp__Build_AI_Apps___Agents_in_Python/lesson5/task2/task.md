# Print the Full Conversation

This script runs a persistent weather assistant that prints every message exchanged in the conversation, labelling each one so it is clear who said what. Human messages are prefixed with `You:` and AI messages with `Agent:`.

The while loop and agent invoke are already written. Add the `for` loop that goes through `response['messages']` and prints each message with the correct label:

1. If `i.type == 'human'`, print `"You: "` followed by `i.content`.
2. If `i.type == 'ai'` and `i.content` is not empty, print `"Agent: "` followed by `i.content`.

Add these lines right after the `agent.invoke(...)` call, before the final `print(response['messages'][-1].content)`.

**Important:** Make sure your `.env` file has your Google API key before running the code.

<div class="hint">

Use a `for i in response['messages']:` loop with two `if` statements inside.

</div>

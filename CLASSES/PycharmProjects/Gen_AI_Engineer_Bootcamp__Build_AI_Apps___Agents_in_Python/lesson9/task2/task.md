# Add Structured Output to an Agent

This script builds an agent that helps with office tasks — specifically, sending emails. When the agent finishes, instead of returning only a plain text message, it also returns a structured `EmailResponse` object with typed fields such as recipient, subject, body, status, and a summary. This makes the agent's output easy to process programmatically.

The agent setup is mostly complete. Two pieces are missing:

1. Add `response_format=EmailResponse` as a keyword argument to `create_agent(...)`.
2. After `agent.invoke(...)`, print the structured response by adding:
   ```python
   print("Structured Response:")
   print(response['structured_response'])
   ```

**Important:** Open the `.env` file and replace the placeholder with your actual Google API key.

<div class="hint">

`response_format` is passed to `create_agent` alongside `model`, `tools`, and `system_prompt`.

</div>

<div class="hint">

The structured result is stored in `response['structured_response']`, not `response['messages']`.

</div>

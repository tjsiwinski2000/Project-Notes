# Complete summarize_with_ai()

This script focuses on the AI core of the spreadsheet automation project. The `summarize_with_ai` function receives raw spreadsheet data as a string and uses an LLM to produce a concise summary — which is then sent by email to the recipient.

Complete the body of `summarize_with_ai(text)`:

1. Define a `system_prompt` string that instructs the model to summarise spreadsheet data concisely.
2. Initialise the model with `init_chat_model("gemini-3-flash-preview", api_key=GEMINI_API_KEY, model_provider="google_genai")` and store it in `model`.
3. Create a `message` list with two dicts: one with `role: "system"` and the system prompt, and one with `role: "user"` and the text as content.
4. Invoke the model with `model.invoke(message).content` and return the result.

**Important:** Add your Gemini API key to the `.env` file before running the code.

<div class="hint">

The message list follows the same pattern used in earlier sections: `[{"role": "system", "content": ...}, {"role": "user", "content": ...}]`.

</div>

<div class="hint">

Call `model.invoke(message)` and access `.content` on the result to get the text string.

</div>

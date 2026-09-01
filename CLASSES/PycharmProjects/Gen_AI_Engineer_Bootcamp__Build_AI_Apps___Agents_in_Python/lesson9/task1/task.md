# Fix the Structured Output Model

This script uses Pydantic models to define a schema for the AI's response. Instead of returning free text, the model returns a structured Python object with typed fields — in this case a list of ingredients and a list of recipe suggestions. The `with_structured_output()` method enforces this schema.

The starter code has two mistakes. Fix them:

1. The model provider is wrong. Change `"openai"` to `"google_genai"`.
2. The wrong class is passed to `with_structured_output`. Change `Recipe` to `Response` — `Response` is the top-level schema that includes both ingredients and the list of recipes.

**Important:** Open the `.env` file and replace the placeholder with your actual Google API key.

<div class="hint">

`model.with_structured_output(...)` takes the Pydantic class that represents the full response shape, not a nested class.

</div>

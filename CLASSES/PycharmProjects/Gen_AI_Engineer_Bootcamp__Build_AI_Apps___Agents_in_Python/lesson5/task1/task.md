# Fix the Persistent Memory Setup

This script improves on the previous memory agent by saving conversation history to a SQLite file on disk. Unlike in-memory storage, the database file persists between separate runs of the program — so the agent still remembers past conversations the next time it is started.

The starter code has two mistakes. Fix them:

1. The model name is wrong. Change `"gemini-1.5-flash"` to `"gemini-3-flash-preview"`.
2. The database filename is wrong. Change `'session.db'` to `'checkpoints.db'`.

Everything else is correct.

**Important:** Make sure your `.env` file has your Google API key before running the code.

<div class="hint">

Both fixes are small value changes — the structure of the code does not need to change.

</div>

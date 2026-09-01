# Fix the Memory Checkpointer

This script extends the weather agent with conversation memory. By passing a `SqliteSaver` checkpointer to the agent, it can remember what was said earlier in the conversation — so the user can ask follow-up questions without repeating themselves. The memory is stored in a local SQLite database file.

The starter code has two mistakes. Fix them:

1. The database filename is wrong. Change `'memory.db'` to `'checkpoints.db'`.
2. The `thread_id` is wrong. Change `"abc"` to `"1"`.

Everything else is correct.

**Important:** Make sure your `.env` file has your Google API key before running the code.

<div class="hint">

`SqliteSaver.from_conn_string(...)` takes the filename of the SQLite database to create or open.

</div>

<div class="hint">

`thread_id` is passed inside the `{"configurable": {...}}` dict as the second argument to `agent.invoke()`.

</div>

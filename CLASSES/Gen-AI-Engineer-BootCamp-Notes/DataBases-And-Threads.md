**0906026**

### Agent v. Threads ###
agent 
- one object, you build it once 
- invoked multiple times.
- each invocation = branches (different thread id)
The agent itself is stateless in terms of conversation history.
The thread_id is what LangGraph uses to look up (and persist)

real world apps
- unique thread ID would be generated for each of those users. It

---
### why database ###
even tho you close the program it behaves as one single session
**HOW** retrieves all the messages from the database anytime you run the program.


### persistant memory ###
1. SQLite is a portable database (file based)
e.g. with SqliteSaver.from_conn_string('checkpoints.db') as checkpointer:
**NOTE1:** 'checkpoints.db' is the SQLite db file. Auto-created if DNE.
**NOTE2:** 'checkpoints.db', checkpoint table, checkpoint field,
human in put saved as BLOB,  can viewed (.)(.) in console (response | messages) 
**NOTE3:** 'checkpoint.db' created when you exit the prompt.  *.wal is working directory

2. SuperBase is based on PostgreSQL,
- standard production database solution (especially for Python)
each app is basically a PROJECT
created tjsiwinski2000_learning

1. Connection string
Copy the connection details for your database.
Details:
Password contains special characters
- percent-encode them in the connection string.

postgresql://postgres.ipxasoyjgndlogkplfsi:AIfofoo%401965@aws-0-us-east-1.pooler.supabase.com:6543/postgres

Supabase
- defaults to ipV6
- ipV4 paid plan or 
Session pooler (port 5432) — good drop-in replacement for direct connections
Transaction pooler (port 6543) — better for short-lived/serverless-style connections
---
2. Install Agent Skills (optional)
Agent Skills give AI coding tools ready-made instructions, scripts, and resources for working with Supabase more accurately and efficiently.



 
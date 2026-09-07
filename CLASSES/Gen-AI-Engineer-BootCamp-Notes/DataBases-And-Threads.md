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

2. SuperBase is based on PostgreSQL,
- standard production database solution (especially for Python)

``` 
	with SqliteSaver.from_conn_string('checkpoints.db') as checkpointer :
    agent = create_agent(
        model=llm,
        tools = [get_weather,get_location],
        system_prompt=system_prompt,
        checkpointer=checkpointer)
```
	
>> So, basically, we're creating an sqlite check pointer
on the fly here,

 
**0905026**

enabling history
- agent actually knows about its previous message 
- CODE: from langgraph.checkpoint.memory import InMemorySaver
```
it's important to remember that if
the invoke method has the same thread ID 
then it will remember about the conversation 
```
THREAD ID CAN BE ANY NUMBER YOUR DEFINE.
ALL RESPONSES WITH THAT THREAD ID CAN BE CONNECTED WITH EACH OTHER.

---
```
Whenever an agent is invoked, the entire list of messages is sent to the LLM.
So not only the latest user query, say again, but say again, plus everything that was previously
so that the AI knows the context, what is going on.
```

various messages that happen when code is run:
- HumanMessage(content='who are you?'
- HumanMessage(content='what is weather in manhattan'
- ToolMessage(content
- Message(content=...

the separate threads do NOT KNOW each other [section 4:22 3;00 min]
---


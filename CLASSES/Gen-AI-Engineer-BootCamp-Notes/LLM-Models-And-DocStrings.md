**0903026**

### trouble with allowances ###
kept running out of free tier usage
```
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

for m in client.models.list():
    if 'lite' in m.name.lower():
        print(m.name)
```
		
#### MODEL OPTIONs ####
- models/gemini-flash-lite-latest
- models/gemini-2.5-flash-lite
- models/gemini-3.1-flash-lite-preview
- models/gemini-3.1-flash-lite
- models/gemini-3.1-flash-lite-image
- models/gemini-3.5-flash-lite
- models/veo-3.1-lite-generate-preview

---
`"""doc strings"""`
- AI agents will read  doc string to understand what this function does.
- "doc strings are CRUCIAL here"

---

```
agent = create_agent(
    model=llm,
    tools = [get_weather]
)

response1 = agent.invoke(
    {"messages": ({'role': 'user',
                   'content':'How is the weather in Rome'})})
print(response1['messages'][-1].content)
```

### WORK FLOW ###
When you invoke this
- query is first sent to the LLM.
- LLM gets the query, and then it decides what function to run.
- Function is combined with the query again, and then it's sent to the LLM
- SO ➡️ TWO LLM calls.
- The first one is just the query.
- The second one is the query plus the results of the function.
- Now this is known as the *REACT*, which means reasoning.
So there is a reasoning part where the LLM tries to find out what function it has to call based on the function doc strings.




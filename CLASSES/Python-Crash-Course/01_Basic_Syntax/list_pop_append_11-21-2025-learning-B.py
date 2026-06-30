#CrashCourse p146 ex8-9,8-10,8-11
def show_messages(list):
    while list:
        msg = list.pop()
        print(msg)
        sent_messages.append(msg)
        

messages=["Dude", "Bruh", "Seriously", "That's Monk"]

sent_messages=[]
#Note: messages[:] sends a COPY of message list
show_messages(messages[:])
print(f"messages: {messages}")
#output is: messages: ['Dude', 'Bruh', 'Seriously', "That's Monk"]
print(f"sent_messages: {sent_messages}")
#output is: sent_messages: ["That's Monk", 'Seriously', 'Bruh', 'Dude'] note: reverse 

#Note: sending ACTUAL list 
show_messages(messages)
print(f"messages: {messages}")
#output is: messages: []
print(f"sent_messages: {sent_messages}")
#output is: sent_messages: ["That's Monk", 'Seriously', 'Bruh', 'Dude', "That's Monk", 'Seriously', 'Bruh', 'Dude']
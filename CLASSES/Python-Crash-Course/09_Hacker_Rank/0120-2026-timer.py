#self assigned challenge
# run as standalone
# python C:\Users\TJ\source\repos\Project-Notes\CLASSES\Python-Crash-Course\09_Hacker_Rank\0120-2026-timer.py
import datetime
import os 
import time


# Get the current date and time
start =  datetime.datetime.now()
for count in range(1,10000):
    current = datetime.datetime.now()
    temp= (current-start)
    print(temp)
    time.sleep(1)
    os.system('cls')
    
    

# print(now)
# timestr = time.strftime("%m%d-%Y-%H%M")
# print(timestr)
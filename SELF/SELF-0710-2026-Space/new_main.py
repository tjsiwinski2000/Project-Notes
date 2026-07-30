# 0710-2026 trying to code cleaner solution
#
# Iterate through space delimated list
# example: 1834672 "C:\Users\All Users\GammaLUTPatch.exe"

my_dict={}
with open('c:\\filesizes.txt') as f1:
    for line in f1:
        if len(line) > 5:
            size = line.split(' ')[0]
            path = line.split(' ')[1]
            my_dict[path] = int(size)

# line below from CLAUDE  not surre why it works TBH
top_10 = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:10])

for entry in top_10:
    print(entry)
    


# EXPLAINING top_10 = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:10]) 

my_dict.items() 
# turns your dict into a list of (path, size) tuples, e.g. [('c:\\a.txt', 30), ('c:\\b.txt', 100), ...]

top_10 = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
# sorts that list of tuples. item[1] means "look at the size (second element) of each tuple to decide order." reverse=True means biggest first.

top_10 = (sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:10]) 
# [:10] — slicing works here because sorted() returns a plain list, and lists support slicing. 
# This grabs just the first 10 tuples (the 10 biggest).

top_10 = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:10]) 
# dict(...) — converts that list of 10 tuples back into a dictionary.
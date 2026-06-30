#0428-2026 creating a random function that is truly random
# testing with theocratic hangman lot of repeats 
import random

results = {}

def create_num():
    temp = random.randint(1, 100)
    temp2 = random.randint(1, 100)
    temp3 = random.randint(1, 100)
    temp4= temp * temp2 / temp3
    if temp4 < 1:
        temp4 = (temp4*20) + random.randint(6,25)
    return  int(temp4)

for i in range(1,101):
    my_next_num= create_num()
    while my_next_num >101:
        my_next_num= create_num()
    results[i] =my_next_num

print(results)

for k,v in results.items():
    print(f"{k}:{v}")
    
    
# print([item for item in results.values()])
from collections import Counter

counts = Counter(results.values())

for number, count in sorted(counts.items()):
    print(f"Number {number}: selected {count} time(s)")

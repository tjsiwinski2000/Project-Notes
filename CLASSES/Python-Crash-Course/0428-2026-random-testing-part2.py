import random


# results = {}
# for i in range(1,101):
#     #create random list, each number appears once
#     numbers = random.sample(range(1, 101), 100)
#     #take random choice from the random list 
#     my_next_num = random.choice(numbers)
#     results[i] =my_next_num

numbers = random.sample(range(1, 101), 100)

from collections import Counter

counts = Counter(numbers)

for number, count in sorted(counts.items()):
    print(f"Number {number}: selected {count} time(s)")

print(numbers)

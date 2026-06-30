import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
index=random.randint(0,4)
print(friends[index])

#another method
print(random.choice(friends))
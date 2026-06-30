# # "npr": {"email": "tjsiwinski_2000@yahoo.com", "password": "+foo-nba"}}
# #===============================
# #===============================
# def find_quote(name):
#     with open('quotes3.txt') as f1:
#         lines=f1.readlines()
#     for line in lines:
#         if name in line.lower():
#             print(line)
            
# find_quote('nadal')

# # Return the most repeated item in a list e.g. a
# my_list = ['a','b','c','a']
# print(max([f'{my_list.count(item)}:{item}' for item in my_list ]))
# print(max(my_list, key=my_list.count))

# # check for palindrome
# s = "A man a plan a canal Panama"

# # remove space and reverse
# print(s.lower().replace(' ','') == s.lower().replace(' ','')[::-1])

# #Target Output: {'quick': 5, 'brown': 5, 'jumps': 5, 'over': 4, 'lazy': 4}
# text = "The quick brown fox jumps over the lazy dog"

# #My soution,set comprehension
# print({f"{item}: {len(item)}" for item in text.split() if len(item) >3}) 

# # However, to get a true dictionary, you don't need the f-string or the 
# # quotes—you just use a colon between the key and the value.
# print({word: len(word) for word in text.split() if len(word) > 3})

# # If the number is even, divide it by 2.
# # If the number is odd, multiply it by 3.
# # Target Output: [3, 1, 9, 2, 5]
# nums = [1, 2, 3, 4, 10]
# # print([num/x for num in nums if num % 2 == 0 x = 2 else x = 3]) # ❌
# print([num // 2 if num % 2 == 0 else num * 3 for num in nums])  

#0424-2026 testing randomness
import random
# 1. Create 100 unique choices (Option 1 to Option 100)
# We use a loop so we don't have to type "A", "B", "C"...
results = {}
for i in range(1, 101):
    results[f"Choice_{i}"] = 0

# 2. Convert the keys into a list so random.choice can use them
options = list(results.keys())

# 3. Run the experiment
# I'll do 1,000 trials so each option has a chance to be picked about 10 times
for _ in range(100):
    pick = random.choice(options)
    results[pick] += 1

# Sorts the dictionary by value (smallest to largest)
sorted_results = sorted(results.items(), key=lambda item: item[1])

# To see both Key and Value
for key, value in sorted_results:
    print(f"{key}: {value}")
    


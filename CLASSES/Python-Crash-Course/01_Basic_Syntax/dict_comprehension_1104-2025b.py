languages ={
    'jen' : 'python',
    'sarah' : 'c',
    'tj' : '.net'
}

# Default iteration is thr. keys
for item in languages:
    print(item)

# Specifying Keys tho. not necessary
for item in languages.keys():
    print(item)

# Iterating thr. values
for item in languages.values():
    print(item)

# Showing both keys, values
for k,v in languages.items():
    print(f"{k} is a key, {v} is a value")
    
#Dictionary Comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split(' ')}
#output {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
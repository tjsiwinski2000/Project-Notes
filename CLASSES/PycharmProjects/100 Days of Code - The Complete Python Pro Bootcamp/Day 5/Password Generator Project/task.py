import random
from random import choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
final_password=""
stemp=""

for number in range(0,nr_letters):
    stemp += random.choice(letters)

for number in range(0,nr_symbols):
    stemp += random.choice(symbols)

for number in range(0,nr_numbers):
    stemp += random.choice(numbers)

#Checkpoint print password before randomization
print(f"Password currently: {stemp}")

#randomize password, this doesn't work since duplicate entries get replaced by ".replace" line e.g. rr
# for number in range(0, len_final_password+1):
#     next_character=random.choice(stemp)
#     final_password += next_character
#     stemp=stemp.replace(next_character,"")
#     if len(stemp) == 0:
#         break
#     print(f"final password currently: {final_password}")

# SOLUTION ONE from AI, shuffle stemp
final_password = "".join(random.sample(stemp,len(stemp)))
print(f"final password version1: {final_password}")

# SOLUTION TWO from AI, and from class , convert to list and shuffle the list
final_password=""
stemp=list(stemp)
random.shuffle(stemp)
#convert list back to string
for char in stemp:
    final_password += char

print(f"final password version2: {final_password}")
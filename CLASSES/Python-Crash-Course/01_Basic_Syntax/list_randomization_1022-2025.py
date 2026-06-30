import art
#print (art.logo)
import random
my_list=['zebra','cow','fox','chicken']

# Make 10 random choices from the above list
for count in range(1,11):
    index = random.randint(0, len(my_list)-1 )
    print(f"{count}.\t random choice is : {my_list[index]}")

  
# Check if entry is in our list    
if "hippo" in my_list:
    print("hippo is in the list")
else:
    print("hippo is NOT in the list")

# Evaluate and Print Boolean one step    
car='toyota'
print(car == 'toyota') #prints True

#Check for empty list
toppings =[]
if toppings:
    for item in toppings:
        print(f"Adding {item}")
else:
    print(("you ordered a plain pizza is that correct?" ))

#Ordinal Numbers
num_list=list(range(1,10))
for num in num_list:
    if num==1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")
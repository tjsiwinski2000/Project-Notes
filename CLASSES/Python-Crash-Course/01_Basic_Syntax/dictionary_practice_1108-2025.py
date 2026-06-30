my_dict ={
    "TJ" : "python",
    "David" : "coffe_talk",
    "Abraham" : "golang",
    "Jake" : "golang"
}

for lang in my_dict.values():
    print(lang)
# python
# coffe_talk
# golang
# golang

#set (remove duplicates)
for lang in set(my_dict.values()):
    print(lang)
# python
# coffe_talk
# golang


my_river_dict = {
    'nile' : 'egypt',
    'mississippli' : 'united states',
    'oh-canada' : 'canada'
}

#print a sentence about each river
for river,country in my_river_dict.items():
    print(f"The {river} runs through {country}")


#loop to print rivers only
for river in my_river_dict.keys():
    print(river)
#loop to print countries only
for country in my_river_dict.values():
    print(country)
    
print('===========\n' *2)  
people =['TJ', 'David', 'Michael']

#6-6 page 105 this is DOPE !
for name in people:
    request_blurb = "Your opinion is important, please take the poll! "
    temp = (my_dict.get(name,request_blurb))
    if temp == request_blurb:
        print(f"{name} {temp}")
    else:
        print(f"Thank you {name} for your response which was {temp}")
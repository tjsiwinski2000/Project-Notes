# Write one-liner to return [1, 2, 3, 4, 5, 6, 7, 8, 9]
nested =[[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print([num for sublist in nested for num in sublist])
# Write one line to return second highest num
my_list = [2, 3, 6, 6, 5]
s=list(sorted(set(my_list)))[-2]
print(s)

# Write a one-liner that returns the most frequent element in a list.
my_list = ['a','b','c','a']
# note: letter should be key; keys must be unique!
my_dict={letter:my_list.count(letter) for letter in my_list}
print(type(my_dict))
# Think of it like a competition — each letter enters the contest, but instead of being judged by its name, it's judged by how many times it appears:
print(max(my_list, key=my_list.count))
# 'a' → count is 2  ← winner
# 'b' → count is 1
# 'c' → count is 1

# #JSON 1)produce this output from data.json (below)
# key: amazon e-mail: tjsiwinski_2000@yahoo.com
# key: mlb e-mail: tjsiwinski_2000@yahoo.com
# 2)add item to local dictionary, 3)post to data.json 
# 4)print out data.json to the screen as a string with read method
# HINT must either LOAD or DUMP json to get it into a variable.
import json
with open("review_data.json") as f1:
    data = json.load(f1)
# This is dope.
# Once you run json.load(f1), 
# Python translates that JSON text into a native Python Dictionary thus ' ❌ "
print(data)
print(f"type of data: {type(data)}")
#must be double quotes to keep JSON "pure"
my_dict["www.jw.org"] = {"email": "tjsiwinski_2000@yahoo.com", "password": "+foo-nba"}
print(f'Updated data {data}')

# json dump (data, file) if you reverse wipes out the file
with open(file="review_data.json",mode='w') as f2:
    json.dump(data,f2)
with open("review_data.json") as f1:
    data = json.load(f1)
print(f'Updated data from file: review_data.json {data}')


# 
# # get output of http://127.0.0.1:5000/random in two lines of code
# -- hint print(requests.get().****)
# given p11 exercise 06-11
cities_dict ={
    "San Diego": {
        "country" : "USA",
        "population" : "1.4 million",
        "fact" : "Balboa Park is amazing."
    },
    "Seoul": {
        "country" : "South Korea",
        "population" : "9.6 million",
        "fact" : "Mom's hometown."
    },
    "Chicago":{
        "country" : "USA",
        "population" : "2.7 million",
        "fact": "Art Institue is awesome"
    }
}
for city, city_info in cities_dict.items():
    print(f"{city} \n\tcountry:{city_info['country']}\n\tpopulation:{city_info['population']}")
#================================================================
string = "abracadabra"
# print 5th character in the string
print(string)
# print(string[4:5])
# change 5th character from a to k using slice
temp = string[:4] + 'k' + string[5:]
print(temp)
s="siwinski"
# return iksniwis and iiiknssw
print(s[::-1])
print(''.join(sorted(s)))
# reverse siwinski -> iksniwis
new_s = ''
new_s = ''.join(s[index] for index in range(len(s)-1, -1, -1))
print(new_s)

# list comprehension, make a list for squares of odd numbers 1-100
print([num**2 for num in range(1,100,2)])

#list practice reference: 01_Basice_Syntax\list_exercise_1014-2025.py
#1014-2025 python practice TJS - Python Crash Course
my_list =["Abraham Lincoln" , "Tony Lazzari", "Helen keller"]
invite_text= "I would like to invite you to dinner at my house."
cant_make="Abraham Lincoln"
first_alternate="Rafael Nadal"
# remove cant_make , add first_alternate @end,  add first_alternate in middle
my_list.remove(cant_make)
my_list.append(first_alternate)
print(my_list)
# make list of even numbers 1-100
print([num for num in range(2,101,2)])
# make list of sqaures 1-100

# slicing a list reference:01_Basice_Syntax\ist_slicing_1017-2025.py
players = ['Rafa', 'Roger', 'Joker', 'Murrary']
# print out Roger, Joker only
print(players[1:3])
# dictionary practice reference:01_Basice_Syntax\dictionary_practice_1021-2025b.py
fruits = {"apple":2, "pear" : 1, "pineaple" : 3, "peach" : 1 , "zebra" : 0 }
# return fruit with highest key e.g. pineapple 3
print(max(fruits,key=fruits.get))
# return fruit with "highest" name  e.g. zebra 
print(max(fruits))

my_list=['zebra','cow','fox','chicken']
# Make 10 random choices from the above list reference: 01_Basice_Syntax\list_randomization_1022-2025.py
import random
for count in range(1,11):
    print(f"{count}. {random.choice(my_list)}")

#Dictionary Comprehension reference: 01_Basice_Syntax\dict_comprehension_1104-2025b.py
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#desired output {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
print([f"{word}:{len(word)}" for word in sentence.split()])
# dictionary practice
my_dict ={
    "TJ" : "python",
    "David" : "coffe_talk",
    "Abraham" : "golang"
}

 print(f"1.raw dictionary")
print(my_dict)

print("#2.sorting a dictionary(Keys)")
print([key for key in sorted(my_dict.keys())])

print('#3.dictionary try,catch')
print(my_dict.get('eric love', 'bro dne'))

print('#4.list values only (in order of insertion)')
print([value for value in (my_dict.values())])

print("#5.list values only (sorted)")
print([value for value in sorted(my_dict.values())])
 
print("#6.list values only but in order of [sorted keys] e.g. Abraham, David, TJ")
print([my_dict[key] for key in sorted(my_dict)])  

#================================================================
#================================================================



#================================================================
#================================================================
import os
NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
NEWS_URL = "https://newsapi.org/v2/everything"

parameters = {
    "q" : "tesla",
    "apikey" : NEWS_API_KEY
}
import requests
response = requests.get(url=NEWS_URL, params=parameters)
response.raise_for_status()
data = response.json()['articles']
# assign data variable the contents of the "article" key 

# print the first three articles
# print(data[:3])
#print  article author, title , url for first three articles
for article in data:
    print(article['title'])
    print(f"\t{article['author']}")
    
#================================================================
#================================================================
# practice review , open file1,file2, create list of numbers in both, create list of numbers in 1, but not 2

list1 = []
list2 = []
list3 = []
list4 = []
file_name1 = "review_ex_nums1.txt"
file_name2 = "review_ex_nums2.txt"

with open(file_name1) as f1:
    for num in f1:
        list1.append(num)
with open(file_name2) as f2:
    for num in f2:
        list2.append(num)

list3 = [num.removesuffix('\n') for num in list1 if num  in list2]
print(list3)
#================================================================
#================================================================
##pg162 Crash Course => complete the class method to show all attributes dynamically
class User:
    def __init__(self, first, last, id, gender, level):
        self.first_name = first
        self.last_name = last 
        self.user_id = id
        self.sex = gender
        self.student_level = level
    
    def describe_user(self):
        #print all attributes of user to screen 1130-2025-learning.py if stuck
        for key, value in self.__dict__.items():
            print(f"{key} : {value}")
        

test_user = User("TJ", "Siwinski", "00001", "male", "freshman")
test_user.describe_user()

##pg124 Crash Course 
# ... while loop pop from unconcirmed to confirmed [see: 1118-2025-new.py]
unconfirmed = ['alice','brian','candace']
confirmed = []

while unconfirmed:
    confirmed.append(unconfirmed.pop())

print(f"confirmed : {confirmed}\nunconfirmed : {unconfirmed}")

# remove all the 'a's with for loop
letters = ['a', 'b', 'a', 'c', 'a' , 'd']
while 'a' in letters:
    letters.remove('a')
print(letters)

#CrashCourse p146 ex8-9,8-10,8-11
# create function show_messages , pass a list, send messages, show resultant list part B: pass a copy of the list 
messages=["Dude", "Bruh", "Seriously", "That's Monk"]
sent_messages=[]

def show_messages(in_list):
    while in_list:
        sent_messages.append(in_list.pop())

print(f"BEFORE messages : {messages}\nsent_messages : {sent_messages}")
show_messages(messages[:])
print(f"AFTER messages : {messages}\nsent_messages : {sent_messages}")

#   NOTE:print(my_dict.get(key)) returns value associated with key cleanly
#----------------------------------------------------------    

#================================================================
#review panda exercise from memory
import pandas
my_data ="review_Squirrel_Data.csv"

data = pandas.read_csv(my_data)


gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])

my_dict = {
    "colors" : ['gray','black','red'],
    "count" : [gray, black, red]
}
my_data_frame =pandas.DataFrame(my_dict)
my_data_frame.to_csv('01252025_sdata.csv')
================================================================
================================================================





# given 
users = {
    'aeinstein' :{
        'first':'albert',
        'last': 'einstein',
        'location' : 'princeton',
    },
    'mcurie' :{
        'first':'marie',
        'last': 'curie',
        'location' : 'paris',
    }
}
# create output  as shown below in two lines of code
# Username: aeinstein
#         Full name: Albert Einstein
#         Location: Princeton
# Username: mcurie
#         Full name: Marie Curie
#         Location: Paris
for user, user_info in users.items():
    print(f"Username: {user}\n\tFull name:{user_info['first'].title()} {user_info['last'].title()}\n\tLocation: {user_info['location']}")

# 0123-2026 this took me for a ride #sal
# Since you are opening a .json file
# For that, you should use the json.load() function:

# import json
# with open("review_data.json", "r") as f1:
#     data = json.load(f1)

# json.dumps returns a string, but it doesn't actually write that 
# string to the file.
# To save your changes to the file, you need to use json.dump() (without the 's').
# The Fix: dump vs dumps
# json.dump(data, f2): Directly Uploads to Memory/Persistence (Writes to a file).
# json.dumps(data): Directly Updates My Python String (Returns a string).

# # Note: You are saving a string inside a dictionary key here
# data['joe.com'] = '{"email": "tjsiwinski_2000@yahoo.com", "password": "+foo-nba"}'
# # Better way: Store as a dictionary, not a string
# data['joe.com'] = {
#     "email": "tjsiwinski_2000@yahoo.com", 
#     "password": "+foo-nba"
# }
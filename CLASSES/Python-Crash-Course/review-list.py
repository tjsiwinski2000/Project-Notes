#07122026
# Write one-liner to return [1, 2, 3, 4, 5, 6, 7, 8, 9]
nested =[[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Write one line to return second highest num
my_list = [2, 3, 6, 6, 5]

# use zip to return [(1, 'a'), (2, 'b'), (3, 'c')]
numbers = [1, 2, 3]
letters = ["a", "b", "c"]


#04062026
# Write a one-liner that returns the most frequent element in a list.
# Print type(intermediate object)
my_list = ['a','b','c','a']

# #JSON 
# 1) output raw content from review_data.json in format below
# key: amazon e-mail: tjsiwinski_2000@yahoo.com
# 2) add item to local dictionary
# 3) print out local dictionary
# 4) update review_data.json
# 5) print out data.json to the screen as a string with read method
# HINT must either LOAD or DUMP json to get it into a variable.
json_file_name = 'review_data.json'

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
#================================================================
string = "abracadabra"
# print 5th character in the string
# change 5th character from a to k using slice

s="siwinski"
# return iksniwis 
# return iiiknssw
# return siwin
# return iksniwis with using slice or reverse
new_s=''

# list comprehension, make a list for squares of odd numbers 1-100
print("squares of odd numbers 1 - 100")
print("")

#list practice reference: 01_Basice_Syntax\list_exercise_1014-2025.py
#1014-2025 python practice TJS - Python Crash Course
my_list =["Abraham Lincoln" , "Tony Lazzari", "Helen keller"]
invite_text= "I would like to invite you to dinner at my house."
cant_make="Abraham Lincoln"
first_alternate="Rafael Nadal"
# remove cant_make , add first_alternate @end,  add first_alternate in middle



# slicing a list reference:01_Basice_Syntax\ist_slicing_1017-2025.py
players = ['Rafa', 'Roger', 'Joker', 'Murrary']
# print out Roger, Joker only

# dictionary practice reference:01_Basice_Syntax\dictionary_practice_1021-2025b.py
fruits = {"apple":2, "pear" : 1, "pineaple" : 3, "peach" : 1 , "zebra" : 0 }
# return fruit with highest VALUE e.g. pineapple 3
# return fruit with "highest" KEY  e.g. zebra 

my_list=['zebra','cow','fox','chicken']
# Make 10 random choices from the above list reference: 01_Basice_Syntax\list_randomization_1022-2025.py


#Dictionary Comprehension reference: 01_Basice_Syntax\dict_comprehension_1104-2025b.py
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#desired output {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

# dictionary practice
my_dict ={
    "TJ" : "python",
    "David" : "coffe_talk",
    "Abraham" : "golang"
}

print(f"1.raw dictionary")


print("#2.sorting a dictionary(Keys)")


print('#3.dictionary try,catch')


print('#4.list values only (in order of insertion)')


print("#5.list values only (sorted)")

 
print("#6.list values only but in order of [sorted keys] e.g. Abraham, David, TJ")

  
#================================================================
#================================================================



#================================================================
#================================================================
NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
NEWS_URL = "https://newsapi.org/v2/everything"

parameters = {
    "q" : "tesla",
    "apikey" : NEWS_API_KEY
}

response = requests.get(url=NEWS_URL, params=parameters)
response.raise_for_status()
# assign data variable the contents of the "article" key 

# print the first three articles

#print  article author, title , url for first three articles

#================================================================
#================================================================
# practice review , open file1,file2, create list of numbers in both, create list of numbers in 1, but not 2

list1 = []
list2 = []
list3 = []
list4 = []
file_name1 = "review_ex_nums1.txt"
file_name2 = "review_ex_nums2.txt"
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
        pass
        

test_user = User("TJ", "Siwinski", "00001", "male", "freshman")
test_user.describe_user()

##pg124 Crash Course 
# ... while loop pop from unconcirmed to confirmed [see: 1118-2025-new.py]
unconfirmed = ['alice','brian','candace']
confirmed = []

# remove all the 'a's with for loop
letters = ['a', 'b', 'a', 'c', 'a' , 'd']
print(letters)

#CrashCourse p146 ex8-9,8-10,8-11
# create function show_messages , pass a list, send messages, show resultant list part B: pass a copy of the list 
messages=["Dude", "Bruh", "Seriously", "That's Monk"]
sent_messages=[]


#================================================================
#review panda exercise from memory
my_data ="review_Squirrel_Data.csv"

gray = "Primary Fur Color" == "Gray"
black = "Primary Fur Color" == "Black"
red = "Primary Fur Color" == "Cinnamon"

#================================================================
#================================================================





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
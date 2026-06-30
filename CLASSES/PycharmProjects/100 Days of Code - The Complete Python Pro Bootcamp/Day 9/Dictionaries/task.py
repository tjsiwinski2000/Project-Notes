programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])
# prints "An error in a program that prevents the program from running as expected."

programming_dictionary["Loop"]= "The action of doing something over and over again"
# assigns a value  to a new key

for key in programming_dictionary:
    print(key) # only prints Bug, Function, Loop NOT the whole entry
    print(programming_dictionary[key])

print(len(programming_dictionary))
# prints 3

programming_dictionary={}
# wipe out the dictionary

print(programming_dictionary)
# prints {}

travel_log ={ "France": ["Paris", "Lille", "Dijon"],}
# dictionary with nested list
print(travel_log["France"])
# prints ["Paris", "Lille", "Dijon"],
print(travel_log["France"][1])
# prints Lille

nl=["a", "b", ["c","d"]]
nl[2][1]
#prints d
travel_log["Germany"]["cities visited"][2]
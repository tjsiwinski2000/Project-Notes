# parameter -  name of the data that's being passed in
# argument  -  actual value of the data.

def greet(name):
    print(f"foo {name}")
#parameter: name ; argument: "tj"
greet("tj")


def life_in_weeks(age):
    total_weeks=90*52
    current_weeks=age*52
    weeks_left=total_weeks-current_weeks
    print(f"You have {weeks_left} weeks left.")
life_in_weeks(56)

def greet_with(name,location):
    print(f"hello {name}")
    print(f"What is it like in {location}")

#postional arguments
greet_with("Jack Bauer", "nowhere")
#keyword arguments
greet_with(location="nowhere",name="Jack Bauer")
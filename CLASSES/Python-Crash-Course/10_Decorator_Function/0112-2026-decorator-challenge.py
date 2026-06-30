# 0112-2026 UDEMY: Python Bootcamp Day55: Exercise23
# Create a logging_decorator() which is going to print the name of the function that was called, the arguments it was given and finally the returned output: 
#     You called a_function(1,2,3) 
#     It returned: 6 

import functools
def logging_decorator(function):
    @functools.wraps(function)
    def wrapper(*args):
        result = f"You called{function.__name__}{args}\nIt returned: {function(*args)}"
        print(result)
        return result
    return wrapper
    


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)
#0112-2026 Lesson 55 , lecture 392
# code was not available [https://replit.com/@appbrewery/python-advanced-decorators#main.py ]
# manual entered code below ... TJS
class User:
    def __init__(self, name): #constructor 
        self.name = name
        self.is_logged_in = False
        
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        #args[0] is first positional argument: [create_blog_post]
        if args[0].is_logged_in == True:
            function(args[0])
        else:
            print("you aint logged in Bro")
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
    
new_user = User("Rachel")
new_user.is_logged_in = False
create_blog_post(new_user)
#1215-2025 exercise 10-14 Verify User p206 in Crash Coursereederdrdeeeerdgddrrrrdrrederee
from pathlib import Path
import json


def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info['username']
    else:
        return None

def get_new_username(path):
    """Prompt for a new username, age, pet"""
    username = input("What is your name? ")
    age = input("What is your age?")
    pet = input("What is your pet's name?")
    user_info ={
        "username" : username,
        "age" : age,
        "pet" : pet        
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def print_summary(user):
    """Output user dictionary"""
    if user:
        for key,value in user.items():
            print(f"{key} : {value}")

def greet_user():
    """Greet the user by name."""
    path = Path('./02_Functions_Classes/1215-2025/username.json')
    username = get_stored_username(path)

    correct_user = "N"
    if username:
        correct_user = input(f"Is your name {username}? , please enter Y or N")
        if correct_user.upper() == 'Y':
            print(f"Welcome back, {username}!")

    
    if username == None or correct_user == "N":
        user_info = get_new_username(path)
        print(f"We'll remember you when you come back, {user_info['username']}!")
        print(f"Thank you for providing background information.")
        print_summary(user_info)

greet_user()
from flask import Flask
import random
import  functools

app = Flask(__name__)

print(__name__)

def set_num_to_guess():
    number_to_guess = random.choice(range(0,10))
    print(f"number to guess {number_to_guess}")
    return number_to_guess

answer=set_num_to_guess()
print(answer)
# route decorator function
# which lives inside app object which is declared in [FLASK class]
@app.route("/")
def hello_world():
    return (f'<h1>Guess a number between 0 and 9</h1>'
            '<img src = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnA1bDYwdGticDh0OTA0cjRlbzR2aGk4bHA1anFpdWQ5Z3ZrOGtiNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kKtfz1PBx4Dz8lvQLE/giphy.gif" width =300>')

@app.route("/<int:guess>")
def compare_guess(guess):
    if answer == guess:
        return  "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'  width =200/>"
    else:
        if guess < answer:
            return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width =200 />"
        else:
            return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width =200/>"


def say_bye():
    return "Bye"

@app.route("/username/<name>/<num>")
def greet(name,num):
    return f"Good Day {name} you are {num} years old !"

#Lines below replaces cmd line "flask run"
if __name__ == "__main__":
    app.run(debug=True)



#NOTE: __main__ this is the current file where the code is located
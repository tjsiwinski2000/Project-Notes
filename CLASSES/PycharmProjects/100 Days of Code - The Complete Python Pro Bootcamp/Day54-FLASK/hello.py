from flask import Flask

app = Flask(__name__)

print(__name__)

import  functools
def make_bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = f"<b>{result}</b>"
        return result
    return wrapper


# route decorator function
# which lives inside app object which is declared in [FLASK class]
@app.route("/")
def hello_world():
    return ("<h1>Hello, World from 11:00am TJ!</h1>"
            "<p>This is a paragraph</p>"
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWI0eGV1MGpjamtwbDhzNm91ZGZ0c3Qxa3kybmthNXFkZHJjMHlqcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zQR7qMJ3Esh0Y/giphy.gif" width =200>')

@app.route("/bye")
@make_bold
def say_bye():
    return "Bye"

@app.route("/username/<name>/<num>")
def greet(name,num):
    return f"Good Day {name} you are {num} years old !"

#Lines below replaces cmd line "flask run"
if __name__ == "__main__":
    app.run(debug=True)

#NOTE: __main__ this is the current file where the code is located
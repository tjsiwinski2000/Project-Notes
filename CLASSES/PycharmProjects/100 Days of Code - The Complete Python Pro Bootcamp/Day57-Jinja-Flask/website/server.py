from flask import Flask, render_template
import random
from datetime import datetime
from agify import get_message
import requests

# instantiates instance of Flask class
# since we run file directly __name__ =  __main__
app = Flask(__name__)

# route decorator function
# insides app OBJECT declared in flask CLASS
@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    return render_template("index.html",num = random_number,year = current_year)


@app.route("/guess/<string:name>")
def greet_name(name):
    user_age, user_name = get_message(name)
    return render_template("index.html", age= user_age, name = user_name)

@app.route("/blog/<int:num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts = all_posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)

#challenge
# http://127.0.0.1:5000/guess/katie
# Hey Katie (title case)
# I think you ae female,
# And maybe 32 years old.

# function to interact with https://agify.io/
# update FLASK app to greet name
# tie it all together
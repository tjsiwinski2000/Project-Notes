from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Using the API for our blog posts we created on n:Point, render all the blogs' title and subtitles on the home page
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    #print(type(all_posts))
    # Pass all_posts [LIST] to template:index.html for display
    return render_template("index.html", posts=all_posts)

@app.route("/post/<int:num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    # Pass all_posts [LIST] and num [id of selected post] to template:post.html for display
    return render_template("post.html", posts = all_posts, num=num)
if __name__ == "__main__":
    app.run(debug=True)




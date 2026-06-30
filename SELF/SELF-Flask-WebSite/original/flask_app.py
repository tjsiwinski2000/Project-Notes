# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import requests
import bs4

app = Flask(__name__)
report = ""
@app.route('/')
def hello_world():
    report=""
    data = requests.get("https://text.npr.org")
    soup = bs4.BeautifulSoup(data.text,"html.parser")
    articles = soup.find_all(name = "a")
    for article in articles:
        t=article.get_text()
        if len(t) > 30:
            report += t +"<br>"
    return f'Hello from Flask!-TS <br> {report}'
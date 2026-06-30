from flask import Flask, render_template

app = Flask(__name__)

print(__name__)

# route decorator function
# which lives inside app object which is declared in [FLASK class]
@app.route("/")
def hello_world():
    return render_template("index.html")

#Lines below replaces cmd line "flask run"
if __name__ == "__main__":
    app.run(debug=True)

#NOTE: __main__ this is the current file where the code is located
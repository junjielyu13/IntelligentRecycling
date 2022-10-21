
from flask import Flask, render_template

app = Flask(__name__,template_folder="../templates",static_folder='../static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/index.html")
def indexhome():
    return index()

if __name__ == "__main__":
    app.run(host="localhost", port="8080", debug=True)
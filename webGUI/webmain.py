from flask import Flask, render_template, send_file
from os import listdir

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("game.html")


@app.route("/models/<typee>/<name>")
def model(typee, name):
    types = listdir("data/models/")
    if typee in types:
        names = listdir("data/models/"+typee)
        if name in names:
            return send_file(f"../data/models/{typee}/{name}")
    return ""



def main():
    app.run()


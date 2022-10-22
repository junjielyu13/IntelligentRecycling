import json

import os

from flask import Flask, render_template, request

app = Flask(__name__,template_folder="../templates",static_folder='../static')


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")



def classification_images(imag):
    pass


@app.route("/identify", methods=['POST', 'GET'])
def indexhome(): 
    check = request.form.get('check')
    if check == "check":
        return "hello world"
    else:
        return json.dumps("nahahaa")



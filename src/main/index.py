import json
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import *



app = Flask(__name__,template_folder="../templates",static_folder='../static')
CORS(app, resources=r'/*')

@app.route("/")
def index():
    return render_template("index.html")


def classification_images(imag):
    pass


@app.route("/identify", methods=['POST'])
def indexhome(): 

    # data = request.get_json()
    # print(data)

    # check = request.form.get('check')


    json = {"status": "400",
            "msg":"success"}

    return "hello world"
    return json.dumps(json)



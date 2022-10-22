import json
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import *



app = Flask(__name__,template_folder="../templates",static_folder='../static')
CORS(app, resources=r'/*')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/identify", methods=['POST'])
def indexhome(): 



    #return "hello world"
    # return flask.jsonify({'msg': 'success'})
    return render_template("index.html")



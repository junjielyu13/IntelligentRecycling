import json
import os
from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import *
from src.main.model_prediction import *
import getpass


app = Flask(__name__, template_folder="../templates",
            static_folder='../static')
# CORS(app, resources=r'/*')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/identify", methods=['POST'])
def identify():

    filename = request.form.get("name")

    print(filename)

    username = getpass.getuser()
    print(username)

    img_path = "C:/Users/" + str(username) + "/Downloads/" + str(filename)
    print(img_path)

    contenedor_value, accuracy = prediction(img_path, im_size=224)

    # return "hello world"
    # return flask.jsonify({'msg': 'success'})
    print(contenedor_value)

    return jsonify({"result": contenedor_value, "perf": accuracy})

    if contenedor_value == "amarillo":
        print("test")
        return redirect("/groc")
    elif contenedor_value == "azul":
        return redirect("/blau")
    elif contenedor_value == "marron":
        return redirect("/marroc")
    elif contenedor_value == "verde":
        return redirect("/verde")
    else:
        return redirect("/gris")


@app.route("/groc")
def groc():
    return render_template("index.html")


@app.route("/blau")
def blau():
    return render_template("blau.html")


@app.route("/marroc")
def marroc():
    return render_template("marro.html")


@app.route("/verde")
def verde():
    return render_template("verd.html")


@app.route("/gris")
def gris():
    return render_template("gris.html")

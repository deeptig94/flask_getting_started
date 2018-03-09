from flask import Flask, jsonify
import math

app = Flask(__name__)

name = "Deepti Gopinath"


@app.route("/name", methods=['GET'])
def name():

    data = {
        "name": name
    }

    return jsonify(data)


@app.route("/hello", methods=['GET'])
def hello_there():

    hello_message = {
        "message": "Hello there, {}".format(name)
    }

    return jsonify(hello_message)


@app.route("/distance", methods=['POST'])
def find_distance():

    a = [2, 4]
    b = [5, 6]

    x = (a[0] - b[0]) ** 2
    y = (a[1] - b[1]) ** 2

    distance = {
        "distance": math.sqrt(x+y),
        "point a": a,
        "point b": b
                }

    return jsonify(distance)

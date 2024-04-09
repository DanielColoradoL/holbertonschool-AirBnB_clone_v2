#!/usr/bin/python3
""" tarts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    Prints a message in the main page
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Prints a message in the /hbnb page
    """
    return "HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

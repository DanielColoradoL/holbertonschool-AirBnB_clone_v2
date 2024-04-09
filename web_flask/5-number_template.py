#!/usr/bin/python3
""" tarts a Flask web application """
from flask import Flask, render_template

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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    display "C " followed by the value of the text
    """
    clean_text = text.replace("_", " ")
    return "C " + clean_text


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    display "Python " followed by the value of the text
    """
    clean_text = text.replace("_", " ")
    return "Python " + clean_text


@app.route("/number/<int:n>", strict_slashes=False)
def num_n(n):
    """
    display “n is a number” only if n is an integer
    """
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template_n(n):
    """
    display a HTML page only if n is an integer
    """
    if isinstance(n, int):
        return render_template("5-number.html", num_n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

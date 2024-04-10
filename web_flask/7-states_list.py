#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """
    Creates a Ul filled with LI
    Based on what's on the DB
    """
    states = storage.all(State)
    print(states)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_db(exc):
    """Close the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

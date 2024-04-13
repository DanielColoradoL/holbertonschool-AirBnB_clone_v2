#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Creates a Ul filled with LI
    Based on what's on the DB
    """
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    Creates a Ul filled with LI
    Based on what's on the DB
    """
    selected_state = None
    states_id = storage.all(State)
    for state in states_id.values():
        if id == state.id:
            selected_state = state
            break
    return render_template("9-states.html", state=selected_state)


@app.teardown_appcontext
def close_db(exc):
    """Close the session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

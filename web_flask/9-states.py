#!/usr/bin/python3
"""
Module for start a web aplication via Flask
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Number_template/<n> page"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    """Number_template/<n> page"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
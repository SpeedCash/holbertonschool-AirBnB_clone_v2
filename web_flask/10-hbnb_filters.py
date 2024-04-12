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


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """display a HTML page like 6-index.html, which was done during the project 0x01. AirBnB clone - Web static"""
    data = {
        "states": storage.all("State").values(),
        "amenities": storage.all("Amenity").values()
    }
    return render_template("10-hbnb_filters.html", models=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#!/usr/bin/python3
"""Moduelf for starts Flask web app"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """Declare a method to handle @app.teardown_appcontext"""
    storage.close()


if __name__ == "__main__":
    app.run(port='5000', host="0.0.0.0")

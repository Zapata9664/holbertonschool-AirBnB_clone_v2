#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_HBNB():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """Display c + text"""
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Display Python + text"""
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route("/number/<int:n>", strict_slashes=False)
def display_int(n):
    """Display a int number"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def display_html(n):
    """Display html"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")

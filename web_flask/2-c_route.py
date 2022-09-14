#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_HBNB():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def print_text(text):
    """Display c + text"""
    text = text.replace('_', ' ')
    return (f"C {text}")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")

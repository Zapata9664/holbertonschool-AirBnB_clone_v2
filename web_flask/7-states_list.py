#!/usr/bin/python3
""""""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_list():
    states = storages.all("State")
    return render_templates("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """"""
    storage.close()



if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
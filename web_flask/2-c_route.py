#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def route():
    """route function to return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_page():
    """route function to return HBNB in hbnb page"""
    return "HBNB"


@app.route("/c/<text>")
def c_page(text):
    """route function to return 'C ' followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    """main function to run"""
    app.run(debug=True, host='0.0.0.0', port=5000)

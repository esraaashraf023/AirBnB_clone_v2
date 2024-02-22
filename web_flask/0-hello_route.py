#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/')
def route():
    """route function to return Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """main function to run"""
    app.run(host='0.0.0.0', port=5000)

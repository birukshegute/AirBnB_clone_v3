#!/usr/bin/python3
""" created a file app.py according to the instructions """

from api.v1.views import app_views
from flask import Flask, jsonify
from os import getenv
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """ declaring teardown method to handle
    @app.teardown_appcontext that calls storage.close() """
    storage.close()


@app.errorhandler(404)
def error(e):
    """a handler for 404 errors that returns a JSON-formatted 404 response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)

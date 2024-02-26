#!/usr/bin/python3
""" creates andex python script """

from api.v1.views import app_views
from models.base_model import BaseModel
import models
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """create a route /status on the object app_views"""
    return jsonify({'status': 'OK'})

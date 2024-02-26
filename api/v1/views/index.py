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


@app_views.route('/stats', methods=['GET'])
def count():
    """ an endpoint that retrieves the number of each objects by type"""
    classes = {"states": "State", "users": "User",
               "amenities": "Amenity", "cities": "City",
               "places": "Place", "reviews": "Review"}
    dic = {}
    for i in classes:
        dic[i] = storage.count(classes[i])
    return jsonify(dic)

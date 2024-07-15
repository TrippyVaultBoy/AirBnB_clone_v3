#!/usr/bin/python3
"""creates a route to status"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_OK():
    """returns a JSON status"""
    return jsonify({"status": "OK", "code": 200}), 200


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """endpoint that retrieves the number of each objects by type"""
    obj_json = {"amenities": storage.count("Amenity"),
                "cities": storage.count("City"),
                "places": storage.count("Place"),
                "reviews": storage.count("Review"),
                "states": storage.count("State"),
                "users": storage.count("User")}
    
    return jsonify(obj_json)

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
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_OK():
    """returns a JSON status"""
    return jsonify({"status": "OK", "code": 200}), 200


@app_views.route("/stats", methods=['GET'], strict_slashes=False)
def stats():
    """endpoint that retrieves the number of each objects by type"""
    obj_json = {"amenities": storage.count("Amenity") or 0,
                "cities": storage.count("City") or 0,
                "places": storage.count("Place") or 0,
                "reviews": storage.count("Review") or 0,
                "states": storage.count("State") or 0,
                "users": storage.count("User") or 0}

    return jsonify(obj_json)

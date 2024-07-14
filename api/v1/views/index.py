#!/usr/bin/python3
"""creates a route to status"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status_OK():
    """returns a JSON status"""
    return jsonify({"status": "OK", "code": 200}), 200


@app_views.route("/api/v1/stats")
def stats():
    """endpoint that retrieves the number of each objects by type"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})

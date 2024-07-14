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
    return jsonify({"amenities": storage.all.count("Amenity"),
                    "cities": storage.all.count("City"),
                    "places": storage.all.count("Place"),
                    "reviews": storage.all.count("Review"),
                    "states": storage.all.count("State"),
                    "users": storage.all.count("User")})

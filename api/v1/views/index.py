#!/usr/bin/python3
"""creates a route to status"""
from api.v1.views import app_views
from flask import Flask, jsonify

@app_views.route("/status")
def status_OK():
    """returns a JSON status"""
    return jsonify({"status": "OK", "code": 200}), 200
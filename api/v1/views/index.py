#!/usr/bin/python3
"""creates a route to status"""
from api.v1.views import app_views

@app_views.route("/status")
def status_OK():
    """returns a JSON status"""
    status = {"status": "OK"}
    return (status.json())
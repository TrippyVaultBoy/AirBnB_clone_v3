#!/usr/bin/python3
from api.v1.views import app_views

@app_views.route("/status")
def status_OK():
    """returns a JSON status"""
    status = {"status": "OK"}
    return (status.json())
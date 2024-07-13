#!/usr/bin/python3
"""It’s time to start your API!"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """handles @app.teardown_appcontext"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """Return a 404 error message"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", threaded=True)

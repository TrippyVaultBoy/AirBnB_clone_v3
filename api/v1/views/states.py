#!/usr/bin/python3
"""Creates a new view for State objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
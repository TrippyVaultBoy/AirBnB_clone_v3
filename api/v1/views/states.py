#!/usr/bin/python3
"""Creates a new view for State objects"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET', 'POST'], strict_slashes=False)
def get_post_states():
    """Handles GET and POST requests for states"""
    if request.method == 'GET':
        all_states = storage.all(State).values()
        return jsonify([state.to_dict() for state in all_states])

    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Not a JSON"}), 400
        if 'name' not in data:
            return jsonify({"error": "Missing name"}), 400
        new_state = State(**data)
        storage.new(new_state)
        storage.save()
        return jsonify(new_state.to_dict()), 201

@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'], strict_slashes=False)
def get_delete_put_state(state_id):
    """Handles GET, DELETE, and PUT requests for a state by id"""
    state = storage.get(State, state_id)
    if not state:
        return jsonify({"error": "Not found"}), 404

    if request.method == 'GET':
        return jsonify(state.to_dict())

    if request.method == 'DELETE':
        storage.delete(state)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            return jsonify({"error": "Not a JSON"}), 400
        for key, value in data.items():
            if key not in ['id', 'created_at', 'updated_at']:
                setattr(state, key, value)
        state.save()
        return jsonify(state.to_dict()), 200

from src.services.users_service import get_users, get_user, add_user, remove_user
from flask import blueprints, jsonify, request

user_blueprint = blueprints.Blueprint('user', __name__)


@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    users = get_users()
    json_data = [user.to_json_dict() for user in users]
    return jsonify(json_data), 200


@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    json_data = user.to_json_dict()
    return jsonify(json_data), 200


@user_blueprint.route('/users', methods=['POST'])
def post_user():
    user = request.get_json()
    if not user:
        return jsonify({"error": "User could not be added"}), 404
    users = get_users()
    if any(u.get_email() == user["email"] for u in users):
        return jsonify({"error": "User already exists"}), 400
    new_user = add_user(user)
    new_user = new_user.to_json_dict()
    return jsonify(new_user), 200


@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    deleted_user = remove_user(user_id)
    if not deleted_user:
        return jsonify({"error": "User could not be deleted"}), 404
    deleted_book = deleted_user.to_json_dict()
    return jsonify(deleted_book), 200

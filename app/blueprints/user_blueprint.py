from flask import Blueprint, request, jsonify
from app.services.user_service import get_user_by_id, create_user

user_bp = Blueprint("user", __name__)

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
    return jsonify({"error": "User not found"}), 404

@user_bp.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user = create_user(data["name"], data["email"])
    return jsonify({"message": "User created", "id": user.id}), 201

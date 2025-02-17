from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from app.models import User
from app.extensions import db

def role_required(required_role):
    """
    Decorator to restrict access based on user roles.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            user_id = get_jwt_identity()
            user = db.session.get(User, user_id)
            
            if not user:
                return jsonify({"message": "User not found"}), 404
            
            if user.role != required_role and user.role != "superadmin":
                return jsonify({"message": "Unauthorized access"}), 403
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def admin_required(func):
    return role_required("admin")(func)

def superadmin_required(func):
    return role_required("superadmin")(func)

def teacher_required(func):
    return role_required("teacher")(func)

def authenticate_user(email, password):
    """
    Authenticates user and returns JWT if credentials are valid.
    """
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None

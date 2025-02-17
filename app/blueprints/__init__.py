from flask import Blueprint

# Import the blueprints
from .auth_blueprint import auth_bp

# Initialize the blueprints
def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
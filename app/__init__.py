from flask import Flask
from app.extensions import db, migrate
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Migrate

    from app.blueprints.user_blueprint import user_bp
    from app.blueprints.evaluation_blueprint import evaluation_bp
    from app.blueprints.report_blueprint import report_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(evaluation_bp)
    app.register_blueprint(report_bp)

    return app
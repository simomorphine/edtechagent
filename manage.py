from flask.cli import FlaskGroup
from flask_migrate import MigrateCommand
from app import create_app, db

app = create_app()
cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    """Creates the database tables."""
    db.create_all()
    print("Database created successfully.")

@cli.command("run")
def run():
    """Runs the Flask application."""
    app.run(debug=True)

if __name__ == "__main__":
    cli()

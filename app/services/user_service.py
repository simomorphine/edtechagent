from app.extensions import db
from app.models import User

def get_user_by_id(user_id):
    return User.query.get(user_id)

def create_user(name, email):
    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return user

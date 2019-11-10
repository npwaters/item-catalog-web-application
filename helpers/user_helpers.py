from flask import Blueprint
from user.models import User
from app import session


user_helpers_app = Blueprint(
    "user_helpers_app",
    __name__
)


def create_new_user(login_session):
    new_user = User(
        name=login_session.get("username"),
        email=login_session.get("email"),
    )
    session.add(new_user)
    session.commit()
    user = session.query(User).filter_by(email=login_session.get("email")).one()
    return user.id


def get_user_info(user_id):
    try:
        return session.query(User).filter_by(id=user_id).one()
    except Exception:
        return None


def get_user_id(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception:
        return None

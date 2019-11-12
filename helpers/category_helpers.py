from flask import Blueprint
from app import session
from category.models import Category


category_helpers_app = Blueprint(
    "category_helpers_app",
    __name__
)


def get_categories():
    try:
        return session.query(Category).all()
    except Exception:
        return

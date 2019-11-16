from flask import Blueprint
from app import session
from category.models import Category
from catalog_item.models import CatalogItem


category_helpers_app = Blueprint(
    "category_helpers_app",
    __name__
)


def get_categories():
    try:
        return session.query(Category).all()
    except Exception:
        return


def get_category(category_name):
    try:
        return session.query(Category).filter_by(
            name=category_name
        ).one()
    except Exception:
        return


def get_category_items(category_id):
    return session.query(CatalogItem).filter_by(
        category_id=category_id
    ).all()



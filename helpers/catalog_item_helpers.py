from flask import Blueprint
from app import session
from catalog_item.models import CatalogItem
from category.models import Category


catalog_item_helpers_app = Blueprint(
    "catalog_item_helpers_app",
    __name__
)


def get_catalog_item(category_name, catalog_item_name):
    category = session.query(Category).filter_by(
        name=category_name
    ).one()

    try:
        return session.query(CatalogItem).filter_by(
            name=catalog_item_name,
            category_id=category.id
        ).one()
    except Exception:
        return


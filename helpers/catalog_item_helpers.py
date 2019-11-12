from flask import Blueprint
from app import session
from catalog_item.models import CatalogItem
from category.models import Category


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


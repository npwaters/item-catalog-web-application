from flask.views import MethodView
from flask import render_template
from app import session
from category.models import Category
from catalog_item.models import CatalogItem
from helpers.category_helpers import get_category, get_category_items


class GetCategoryItems(MethodView):

    def dispatch_request(self, category_name):
        categories = session.query(Category).all()
        category = get_category(category_name)
        catalog_items = get_category_items(category.id)
        return render_template(
            "category_items.html",
            categories=categories,
            category=category,
            category_items=catalog_items
        )

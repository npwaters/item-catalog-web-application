from flask.views import MethodView
from flask import render_template
from app import session
from category.models import Category
from catalog_item.models import CatalogItem


class GetCategoryItems(MethodView):

    def dispatch_request(self, category_name):
        categories = session.query(Category).all()
        category = session.query(Category).filter_by(name=category_name).one()
        catalog_items = session.query(CatalogItem).filter_by(
            category_id=category.id
        ).all()
        return render_template(
            "category_items.html",
            heading=category_name,
            categories=categories,
            category=category,
            category_items=catalog_items
        )

from flask.views import MethodView
from flask import render_template
from app import session
from category.models import Category
from catalog_item.models import CatalogItem


class ShowHomePage(MethodView):

    def dispatch_request(self, *args, **kwargs):
        latest_items = 2
        categories = session.query(Category).all()
        latest_catalog_items = session.query(CatalogItem)\
            .order_by(CatalogItem.id.desc())\
            .limit(latest_items).all()
        return render_template(
            "main_nav.html",
            categories=categories,
            latest_catalog_items=latest_catalog_items,
            heading="Latest Items",
        )

from flask.views import MethodView
from flask import render_template
from app import session, login_session
from catalog_item.models import CatalogItem
from category.models import Category


class GetCatalogItem(MethodView):

    def dispatch_request(self, category_name, catalog_item_name):
        category = session.query(Category).filter_by(
            name=category_name
        ).one()

        catalog_item = session.query(CatalogItem).filter_by(
            name=catalog_item_name,
            category_id=category.id
        ).one()
        return render_template(
            "read_catalog_item.html",
            catalog_item=catalog_item,
            STATE=login_session.get("state"),
            user=login_session.get("username")
        )

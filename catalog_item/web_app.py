from flask.views import MethodView
from flask import render_template
from app import session, login_session
from helpers.catalog_item_helpers import get_catalog_item


class GetCatalogItem(MethodView):

    def dispatch_request(self, category_name, catalog_item_name):
        catalog_item = get_catalog_item(
            category_name,
            catalog_item_name
        )
        return render_template(
            "read_catalog_item.html",
            catalog_item=catalog_item,
            STATE=login_session.get("state"),
            user=login_session.get("username")
        )

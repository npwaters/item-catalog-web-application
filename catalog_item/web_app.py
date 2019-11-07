from flask.views import MethodView
from flask import render_template
from app import session
from catalog_item.models import CatalogItem


class GetCatalogItem(MethodView):

    def dispatch_request(self, category_name, catalog_item_name):
        catalog_item = session.query(CatalogItem).filter_by(
            name=catalog_item_name
        ).one()
        return render_template(
            "read_catalog_item.html",
            catalog_item=catalog_item
        )

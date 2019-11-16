from flask import Blueprint
from catalog.api import CatalogAPI


catalog_app = Blueprint(
    "catalog_app",
    __name__
)

# api
get_catalog_api_view = CatalogAPI.as_view(
    "get_catalog_api_view"
)

catalog_app.add_url_rule(
    "/catalog/items",
    view_func=get_catalog_api_view,
    methods=["GET", ]
)


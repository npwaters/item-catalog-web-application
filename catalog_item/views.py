from flask import Blueprint
from catalog_item.web_app import (
    GetCatalogItem,
    EditCatalogItem,
    CreateCatalogItem,
    DeleteCatalogItem
)


catalog_item_app = Blueprint(
    "catalog_item_app",
    __name__,
    template_folder="blueprint_templates/catalog_item"
)

# web app
create_catalog_item_web_view = CreateCatalogItem.as_view(
    "create_catalog_item_web_view"
)
get_catalog_item_web_view = GetCatalogItem.as_view(
    "get_catalog_item_web_view"
)
edit_catalog_item_web_view = EditCatalogItem.as_view(
    "edit_catalog_item_web_view"
)
delete_catalog_item_web_view = DeleteCatalogItem.as_view(
    "delete_catalog_item_web_view"
)

catalog_item_app.add_url_rule(
    "/catalog/new",
    view_func=create_catalog_item_web_view,
    methods=["GET", "POST", ]
)
catalog_item_app.add_url_rule(
    "/catalog/<category_name>/items/<catalog_item_name>",
    view_func=get_catalog_item_web_view,
    methods=["GET", ]
)
catalog_item_app.add_url_rule(
    "/catalog/<category_name>/<catalog_item_name>/edit",
    view_func=edit_catalog_item_web_view,
    methods=["GET", "POST", ]
)
catalog_item_app.add_url_rule(
    "/catalog/<category_name>/<catalog_item_name>/delete",
    view_func=delete_catalog_item_web_view,
    methods=["GET", "POST", ]
)

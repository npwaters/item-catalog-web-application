from flask import Blueprint
from category.web_app import GetCategoryItems


category_app = Blueprint(
    "category_app",
    __name__,
    template_folder="blueprint_templates/category"
)

# web app
get_category_items_web_view = GetCategoryItems.as_view(
    "get_category_items_web_view"
)

category_app.add_url_rule(
    "/catalog/<category_name>/items",
    view_func=get_category_items_web_view,
    methods=["GET", ]
)

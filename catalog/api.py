from flask.views import MethodView
from flask import request, abort, jsonify
from helpers.category_helpers import get_categories, get_category_items


class CatalogAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET' and request.method != 'DELETE') \
                and not request.json:
            abort(400)

    def get(self):
        categories = [
            category.serialize for category in get_categories()
        ]
        for category in categories:
            category["catalog_items"] = [
                catalog_item.serialize for catalog_item in
                get_category_items(category.get("id"))
            ]
        return jsonify(categories)


from flask.views import MethodView
from flask import render_template, jsonify, request, redirect, url_for
from app import session, login_session
from helpers.catalog_item_helpers import get_catalog_item
from helpers.category_helpers import get_categories, get_category


class GetCatalogItem(MethodView):

    def dispatch_request(self, category_name, catalog_item_name):
        catalog_item = get_catalog_item(
            category_name,
            catalog_item_name
        )
        category = get_category(category_name)
        return render_template(
            "read_catalog_item.html",
            catalog_item=catalog_item,
            category=category,
            STATE=login_session.get("state"),
            user=login_session.get("username")
        )


class EditCatalogItem(MethodView):

    def dispatch_request(self, category_name, catalog_item_name):
        catalog_item = get_catalog_item(
            category_name,
            catalog_item_name
        )
        if not catalog_item:
            # TODO: render a 404 error page
            return jsonify({}), 404
        if request.method == "GET":
            categories = get_categories()
            return render_template(
                "edit_catalog_item.html",
                catalog_item=catalog_item,
                category_name=category_name,
                categories=categories,
            )
        else:
            catalog_item_form = request.form
            if catalog_item_form.get("name"):
                catalog_item.name = catalog_item_form.get("name")
            session.add(catalog_item)
            session.commit()
            return redirect(url_for(
                "category_app.get_category_items_web_view",
                category_name=category_name
                )
            )



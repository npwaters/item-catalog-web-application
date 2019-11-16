from flask.views import MethodView
from flask import render_template, jsonify, request, redirect, url_for
from app import session, login_session
from catalog_item.models import CatalogItem
from helpers.catalog_item_helpers import get_catalog_item
from helpers.category_helpers import get_categories, get_category


class CreateCatalogItem(MethodView):

    def dispatch_request(self):
        if request.method == "GET":
            categories = get_categories()
            return render_template(
                "create_catalog_item.html",
                categories=categories
            )
        else:
            catalog_item = CatalogItem()
            catalog_item_form = request.form
            if catalog_item_form.get("name"):
                catalog_item.name = catalog_item_form.get("name")
            if catalog_item_form.get("description"):
                catalog_item.description = catalog_item_form.get("description")
            category = get_category(
                catalog_item_form.get("category")
            )
            catalog_item.category_id = category.id
            catalog_item.user_id = login_session.get("user_id")
            session.add(catalog_item)
            session.commit()
            return redirect(url_for(
                "home_app.show_home_page_web"
            ))


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


class DeleteCatalogItem(MethodView):

    def dispatch_request(self, category_name, catalog_item_name):
        catalog_item = get_catalog_item(
            category_name,
            catalog_item_name
        )
        if not catalog_item:
            return jsonify({}), 404
        category = get_category(category_name)
        if request.method == "GET":
            return render_template(
                "delete_catalog_item.html",
                category=category,
                catalog_item=catalog_item
            )
        else:
            session.delete(catalog_item)
            session.commit()
            return redirect(url_for(
                "category_app.get_category_items_web_view",
                category_name=category.name
            ))


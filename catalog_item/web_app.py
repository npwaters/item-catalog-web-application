from flask.views import MethodView
from flask import render_template, jsonify, request, redirect, url_for, flash
from app import session, login_session
from catalog_item.models import CatalogItem
from helpers.catalog_item_helpers import get_catalog_item
from helpers.category_helpers import get_categories, get_category


NEED_TO_BE_OWNER_RESPONSE = (
    '<script>'
    'function alertFunction() {'
    'alert("Only the item owner is authorised to perform that action!");'
    'path_items = window.location.pathname.split("/");'
    'path_items = path_items.slice(0, -1);'
    'len = path_items.length;'
    'path_items.splice(len - 1, 0, "items");'
    'window.location.href = path_items.join("/");'
    '};'
    '</script><body onload="alertFunction()">'
)
NEED_TO_BE_LOGGED_IN_RESPONSE = (
    "<script>function alertFunction() {"
    "alert('You need to login to perform that action!');"
    "window.location.href = '/';"
    ";}</script><body onload='alertFunction()'>"
)


class CreateCatalogItem(MethodView):

    def dispatch_request(self):
        if "username" not in login_session:
            # display and alert and redirect to home page
            # on clicking OK.
            return NEED_TO_BE_LOGGED_IN_RESPONSE

        if request.method == "GET":
            categories = get_categories()
            return render_template(
                "create_catalog_item.html",
                categories=categories
            )
        else:
            catalog_item = CatalogItem()
            catalog_item_form = request.form
            new_item_name = catalog_item_form.get("name")
            if new_item_name:
                catalog_item.name = catalog_item_form.get("name")
            category = get_category(
                catalog_item_form.get("category")
            )
            # check if the already a catalog_item with the same
            # name in this category
            existing_catalog_item = get_catalog_item(
                category.name,
                new_item_name
            )
            if existing_catalog_item:
                # add flash message
                flash(
                    "A catalog item with the name {0} already exists"
                    " in category {1}".format(new_item_name, category.name),
                    "error"
                )
                return redirect(url_for(
                    "category_app.get_category_items_web_view",
                    category_name=category.name
                ))
            if catalog_item_form.get("description"):
                catalog_item.description = catalog_item_form.get("description")

            catalog_item.category_id = category.id
            catalog_item.user_id = login_session.get("user_id")
            session.add(catalog_item)
            session.commit()
            flash(
                "Catalog item {0} successfully created"
                " in category {1}".format(new_item_name, category.name),
                "success"
            )
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
        if "username" not in login_session:
            # display and alert and redirect to home page
            # on clicking OK.
            return NEED_TO_BE_LOGGED_IN_RESPONSE
        if login_session.get("user_id") != catalog_item.user_id:
            return NEED_TO_BE_OWNER_RESPONSE

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
            if catalog_item_form.get("description"):
                catalog_item.description = catalog_item_form.get("description")
            category = get_category(
                catalog_item_form.get("category")
            )
            catalog_item.category_id = category.id

            session.add(catalog_item)
            session.commit()
            flash(
                "Catalog item {0} successfully updated".format(catalog_item.name),
                "success"
            )
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
        if "username" not in login_session:
            # display and alert and redirect to home page
            # on clicking OK.
            return NEED_TO_BE_LOGGED_IN_RESPONSE
        if login_session.get("user_id") != catalog_item.user_id:
            return NEED_TO_BE_OWNER_RESPONSE

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
            flash(
                "Catalog item {0} successfully removed"
                " from category {1}".format(catalog_item.name, category.name),
                "success"
            )
            return redirect(url_for(
                "category_app.get_category_items_web_view",
                category_name=category.name
            ))


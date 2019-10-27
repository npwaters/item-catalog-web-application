from flask import Blueprint

from home.web_app import ShowHomePage


home_app = Blueprint("home_app", __name__)

show_home_page_view_web = ShowHomePage.as_view("show_home_page_web")

home_app.add_url_rule(
    "/",
    view_func=show_home_page_view_web,
    methods=["GET", ]
)

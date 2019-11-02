from flask import Blueprint
from category.web_app import CreateNewCategory


category_app = Blueprint("category_app", __name__)

from flask import Blueprint
from catalog_item.web_app import CreateNewCatalogItem


catalog_item_app = Blueprint("catalog_item_app", __name__)

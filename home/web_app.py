from flask.views import MethodView
from app import session
from category.models import Category
from catalog_item.models import CatalogItem


class ShowHomePage(MethodView):

    def dispatch_request(self, *args, **kwargs):
        latest_items = 2
        categories = session.query(Category).all()
        latest_catalog_items = session.query(CatalogItem).limit(latest_items).all()
        return "Hello World!!"

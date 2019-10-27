from flask.views import MethodView


class ShowHomePage(MethodView):

    def dispatch_request(self, *args, **kwargs):
        return "Hello World!!"

import random
import string
from flask import Blueprint, current_app, request
from app import login_session
from authentication.web_app import ProcessOAuthLogin

authentication_app = Blueprint(
    "authentication_app",
    __name__
)

process_oauth_login_web_view = ProcessOAuthLogin.as_view(
    "process_oauth_login_web_view"
)

authentication_app.add_url_rule(
    "/google_login",
    view_func=process_oauth_login_web_view,
    methods=["POST", ]
)


@authentication_app.before_app_request
def generate_anti_forgery_session_token():
    if "/static/" not in str(request.url) and "favicon" not in str(request.url)\
            and "/google_login" not in str(request.url):
        print("generating anti-forgery token!")
        state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for x in range(32))
        login_session['state'] = state


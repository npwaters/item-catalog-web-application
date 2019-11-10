import random
import string
from flask import Blueprint, current_app
from app import login_session


authentication_app = Blueprint(
    "authentication_app",
    __name__
)


@authentication_app.before_app_request
def generate_anti_forgery_session_token():
    print("generating anti-forgery token!")
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state


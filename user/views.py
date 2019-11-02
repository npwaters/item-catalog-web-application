from flask import Blueprint
from user.web_app import CreateNewUser


user_app = Blueprint("user_app", __name__)

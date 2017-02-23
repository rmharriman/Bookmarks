from flask import Blueprint


# first thing to do is create bp instance
main = Blueprint("main", __name__)

from . import views

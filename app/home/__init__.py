from flask import Blueprint

home = Blueprint('home', __name__, url_prefix='/dashboard')

from . import views

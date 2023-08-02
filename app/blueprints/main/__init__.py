from flask import Blueprint

bp = Blueprint('main', __name__)

from app.blueprints.main import routes
# The above is the path showing that we are importing from the following:
# app --> blueprints --> main --> routes.py
from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

from app.blueprints.auth import routes
# This is saying we're importing routes.py from:
# app --> blueprints --> auth --> routes.py

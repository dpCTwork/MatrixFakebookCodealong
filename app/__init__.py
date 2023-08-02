from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app) # This is the database object instance
migrate = Migrate(app, db) # This is the migration engine instance, where we pass in the app and the database object instance
login = LoginManager(app) # This is the login manager instance, where we pass in the app

# The following is saying that if a user tries to access a page that requires them to be logged in,
# and they are not logged in, then they will be redirected to the login page.
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
login.login_message_category = 'warning'

from app.blueprints.auth import bp as auth_bp
app.register_blueprint(auth_bp)
from app.blueprints.main import bp as main_bp
app.register_blueprint(main_bp)
from app.blueprints.social import bp as social_bp
app.register_blueprint(social_bp)
from app.blueprints.api import bp as api_bp
app.register_blueprint(api_bp)

from app import models
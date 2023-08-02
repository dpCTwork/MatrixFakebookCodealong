# After we get SQLAlchemy and instantiated it (as 'db'), we can start setting up our SQL tables via python class in app/models.py
# This is where we create our database models

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from secrets import token_urlsafe




# Start by importing db from app/__init__.py
# Any time we do anything with db now, we need to put it above this line in order to avoid circular imports
# This is because we're importing db from app/__init__.py, and we're importing User from app/models.py
from app import db, login

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    # This is the User table. We are creating a table called 'User' with the following columns:
    # user_id, username, email, and password
    # The user_id is the primary key, which means it is the unique identifier for each user
    # First you pass in the datatype, then state whether it's a primary key or not. Default is False.
    user_id = db.Column(db.Integer, primary_key=True)
    # We'll also set the username and email to be unique.
    # The unique=True means that the username/email must be unique. No two users can have the same username/email.
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    token = db.Column(db.String(250), unique=True)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        # This is the string representation of the User object.
        # This is what will be returned when we query the database for a User object.
        return f'User: {self.username}'
    
    def commit(self):
        # This is a method that commits the User object to the database.
        # We will call this method in our routes.py file.
        db.session.add(self)
        db.session.commit()

    def hash_password(self, password):
        # This method will hash the password
        return generate_password_hash(password)
    
    def check_password(self, password):
        # This method will check the password
        return check_password_hash(self.password, password)
    
    def add_token(self):
        # This method will add a token to the database
        # We will call this method in our routes.py file.
        
        # Dylan's code
        setattr(self, 'token', token_urlsafe(32))
        
        # GitHub CoPilot suggested this code:
        # self.token = self.generate_token()
        # self.commit()


    def get_id(self):
        return str(self.user_id)
        
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return f'Post: {self.body}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
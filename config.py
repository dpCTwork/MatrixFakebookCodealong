import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI is a preset configuration variable for flask_sqlalchemy,
    # but we saved the database URL in the .env file as 'DATABASE_URL', 
    # so that's why we have to use os.environ.get('DATABASE_URL') instead of os.environ.get('DATABASE_URI')

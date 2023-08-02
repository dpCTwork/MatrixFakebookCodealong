from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class PostForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired()])
    submit = SubmitField('Publish')

class UserSearchForm(FlaskForm):
    user = StringField('User', validators=[DataRequired()])
    submit = SubmitField('Search')    
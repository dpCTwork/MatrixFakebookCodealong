from flask import render_template, g
from . import bp

from app import app
from app.forms import UserSearchForm

@app.before_request
def before_request():
    g.user_search_form = UserSearchForm()

@bp.route('/')
def home():
    matrix = {
        'instructors': ('Sean', 'Dylan'),
        'students': ['Ray', 'Ben', 'Christopher', 'Alec']
        }
    return render_template('index.j2', title='Home', instructors=matrix['instructors'], students=matrix['students'], user_search_form=g.user_search_form)

@bp.route('/about')
def about():
    return render_template('about.j2', title='About', user_search_form=g.user_search_form)
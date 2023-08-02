from flask import render_template, flash, redirect, url_for, g
from flask_login import current_user, login_required
from . import bp

from app.models import Post, User
from app.forms import PostForm, UserSearchForm

@bp.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(body=form.body.data)
        p.user_id = current_user.user_id
        p.commit()
        # redirecting to user page
        flash(f'Post successfully published!', 'success')
        return redirect(url_for('social.user_page', username=current_user.username))
    return render_template('post.j2', title='Post', form=form, user_search_form=g.user_search_form)

@bp.route('/user-page/<username>')
@login_required
# We can use hyphen instead of underscore because this is just an endpoint that we're specifying to access a user's page.
def user_page(username):
    # We're going to query the database for the user's posts.
    # We'll use the filter_by() method to filter the posts by the user's username.
    # Can also query by user_id, email, etc.
    user = User.query.filter_by(username=username).first()
    return render_template('userpage.j2', title=f"{username}'s Page", user=user, user_search_form=g.user_search_form)

@bp.post('/user-search')
# Because we're only using the post method, and 'post' is in the route, we can do bp.post instead of bp.route
@login_required
def user_search():
    if g.user_search_form.validate_on_submit():
        return redirect(url_for('social.user_page', username=g.user_search_form.user.data))
    return redirect(url_for('main.home'))
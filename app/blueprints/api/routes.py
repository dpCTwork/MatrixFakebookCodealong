from flask import request, jsonify

from . import bp
from app.models import Post, User
from app.blueprints.api.helpers import token_required
# Can also just do 
# from .helpers import token_required


# Receive all posts
@bp.route('/posts', methods=['GET'])
# @bp.get('/posts')  # This is the same as the above
# This '/posts' (which is going to the database) is different from the social_posts route in routes.py (which is going to the front end)
@token_required
def api_posts(user):
    result = []
    posts = Post.query.all()
    for post in posts:
        result.append({
            'id': post.id,
            'body': post.body, 
            'timestamp': post.timestamp,
            'author': post.author.username,
            'user_id': post.user_id
            })
    return jsonify(result), 200

# Receive posts from single user
@bp.get('/posts/<username>')
@token_required
def api_user_posts(user, username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify([{
            'id': post.id,
            'body': post.body, 
            'timestamp': post.timestamp,
            'author': post.author.username,
            'user_id': post.user_id
            } for post in user.posts]), 200 # This is a list comprehension. Also don't *need* '200' because that's the default.
    return jsonify({'message': 'User not found.'}), 404 # 404 is the error code for 'not found'

# Send a single post
@bp.get('/post/<post_id>')
@token_required
def get_post(user, post_id):
    try:
        post = Post.query.get(post_id)
        return jsonify([{
            'id': post.id,
            'body': post.body, 
            'timestamp': post.timestamp,
            'author': post.author.username,
            'user_id': post.user_id
            }]), 200
    except:
        return jsonify({'message': 'Post not found.'}), 404
    

# Create a new post

@bp.post('/post/')
@token_required
def create_post(user):
    try:
        # Receive their post data
        content = request.get_json()
        
        # Create a new post instance or entry
        # Add foreign key to the user_id
        #Dylan's Code
        post = Post(body=content.get('body'), user_id=user.user_id)

        # GitHub CoPilot suggested this code:
        post = Post(body=content['body'], user_id=user.user_id)
        
        # Commit to the database
        post.commit()
        
        # Return a message
        return jsonify({'message': 'Post created.', 'body':post.body}), 201 # 201 is the error code for 'created'
    except:
        jsonify({'message': 'Invalid form data.'}), 400 # 400 is the error code for 'bad request'



# The following will be in our 'auth_routes.py' file
# Verify that the user is the user in database
# Register a new user

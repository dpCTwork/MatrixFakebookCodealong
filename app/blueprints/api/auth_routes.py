from flask import request, jsonify

from . import bp
from app.models import User

# Verify user

@bp.post('/verify') # This is the same as @bp.route('/verify', methods=['POST'])
def verify():
    content = request.get_json()
    print(content)
    username = content['username']
    password = content['password']
    user = User.query.filter_by(username=username).first()
    # user = User.query.filter_by(username=content['username']).first() # This is the same as the above if we didn't save the data to a variable
    
    # Dylan's code:
    # if user and user.check_password(password):
    #     return jsonify([{'user id': user.user_id}])
    
    # GitHub CoPilot suggested this code:
    if user:
        if user.check_password(password):
            return jsonify({'user token': user.token}), 200
        return jsonify({'message': 'Incorrect password.'}), 400
    return jsonify({'message': 'User not found.'}), 404

# Register a new user
@bp.post('/register') # This is the same as @bp.route('/register', methods=['POST'])
def register():
    content = request.get_json()
    print(content)
    username = content['username']
    email = content['email']
    password = content['password']
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'message': 'Username already exists.'})
    user_email = User.query.filter_by(email=email).first()
    if user_email:
        return jsonify({'message': 'Email already taken. Try again.'})
    user = User(username=username, email=email)
    # user.password = user.hash_password(password)
    setattr(user,'password',user.hash_password(password)) # This is the same as the above, using built in Python function setattr()
    user.add_token()
    user.commit()
    print(user)
    return jsonify({'message': f"User {user.username} created."})
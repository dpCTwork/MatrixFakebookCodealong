from flask import request, jsonify
from functools import wraps

from app.models import User


def token_required(flask_route):
    @wraps(flask_route)
    def wrapper(*args, **kwargs):
        if 'x-access-token' in request.headers:
            # The request header would show a value of this: 
            # 'Bearer <token>'
            # We only want the token itself, so we split the string and take the last item in the list, which is the token
            try:
                token = request.headers['x-access-token'].split()[1]
                user = User.query.filter_by(token=token).first()
                if user:
                    return flask_route(user, *args, **kwargs)
                return jsonify({'message': 'Invalid token.'}), 401
            except:
                return jsonify({'message': 'Invalid token.'}), 401
        return jsonify({'message': 'Token is missing.'}), 401
    return wrapper


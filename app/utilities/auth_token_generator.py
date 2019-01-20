"""Module for all User authentication"""
import os
from functools import wraps

import jwt
from app.auth.v2.models import UserModel
from flask import request


class Authenticate:
    """Class to authenticate all users"""

    def token_required(f):
        """User login authentication decorator"""

        @wraps(func)
        def decorated(*args, **kwargs):
            """User login authentication decorator"""
            access_token = None
            try:
                authorization_header = request.headers.get('Authorization')
                if authorization_header:
                    access_token = authorization_header.split(' ')[1]
                if access_token:
                    user_email = UserModel.decode_token(access_token)['email']
                    return func(user_email=user_email, *args, **kwargs)
                return {
                    "status": 401,
                    "message":
                    "Please login first, your session might have expired"}, 401
            except Exception as e:
                return {
                    "status": 400,
                    "message":
                    "An error occurred while decoding token.",
                    "error": str(e)}, 400
        return decorated

    def admin_required(self):
        """Admin authentication decorator"""
        @wraps(f)
        def admin_auth(*args, **kwargs):
            """Admin authentication decorator"""
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
                try:
                    data = jwt.decode(
                        token,
                        os.getenv("SECRET_KEY"),
                        algorithm='HS256'
                    )
                except jwt.ExpiredSignatureError:
                    return {
                        "status": 401,
                        "error": "Login expired. Please login again"
                    }, 401
                except jwt.InvalidTokenError:
                    return {
                        "status": 401,
                        "error": "Invalid token. Please login again"
                    }, 401
                user = UserModel.check_for_admin(self, data['email'])
                if user:
                    return f(current_user=data['email'], *args, **kwargs)
            else:
                return {
                    "status": 401,
                    "error": "You are not authorized to perform this action"
                }, 401
        return admin_auth

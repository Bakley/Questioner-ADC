"""Module for all User authentication"""
import os
import jwt
from functools import wraps
from flask import request, current_app
# from app.auth.v2.models import UserModel
# from app.auth.v2.views import valid_admin


def token_required(func):
    """User login authentication decorator"""

    @wraps(func)
    def user_auth(*args, **kwargs):
        """User login authentication decorator"""
        if 'Bearer' in request.headers:
            token = request.headers['Bearer']
            try:
                data = jwt.decode(
                    token,
                    str(current_app.config.get('SECRET')),
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
                    "error": "Invalid token user. Please login again"
                }, 401

            return func(current_user=data['email'], *args, **kwargs)
        else:
            return {
                "status": 401,
                "error": "You are not logged in"
            }, 401
    return user_auth


def admin_required(f):
    """Admin authentication decorator"""

    @wraps(f)
    def admin_auth(*args, **kwargs):
        """Admin authentication decorator"""
        if 'Bearer' in request.headers:
            token = request.headers['Bearer']
            print("Admin token", token)
            try:
                data = jwt.decode(
                    token,
                    os.getenv("SECRET_KEY"),
                    algorithm='HS256'
                ).decode('UTF-8')
            except jwt.ExpiredSignatureError:
                return {
                    "status": 401,
                    "error": "Login expired. Please login again"
                }, 401
            except jwt.InvalidTokenError as e:
                print("hello", e)
                return {
                    "status": 401,
                    "error": "Invalid token Admin. Please login again"
                }, 401

            # user = UserModel.check_for_admin(self, data['email'])
            print("Admin", user)
            if user:
                return f(*args, **kwargs, current_user=data['email'])
        else:
            return {
                "status": 401,
                "error": "You are not authorized to perform this action"
            }, 401
    return admin_auth

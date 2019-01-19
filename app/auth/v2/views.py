from flask_restful import Resource
from flask import make_response,jsonify, request
from app.auth.v2.models import UserModels

user_view = UserModels()

class SignUp(Resource):
    """User view class to register"""

    def post(self):
        """Method to register a user, POST verb"""
        data = request.get_json()
        email = data['email']
        new_user = user_view.create_a_user(email)
        return {
            "user":new_user
        }
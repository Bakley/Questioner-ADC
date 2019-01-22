import os
import jwt
from datetime import datetime, timedelta
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app.api.v2.dbmodel import QuestionerDb


class UserModel:
    """Class for the user models"""

    def create_user(self, firstname, lastname, othername, username, userpassword, email, phoneNumber):
        hashed_password = generate_password_hash(userpassword)
        email_query = """SELECT * FROM users WHERE email = '{}'""".format(
            email)
        duplicate_email = QuestionerDb.retrieve_all(email_query)
        if duplicate_email:
            return False
        user_query = """INSERT INTO users
                    (firstname, lastname, othername,
                    username, userpassword, email, phonenumber)
                    VALUES(%s, %s, %s, %s, %s, %s, %s)
                    RETURNING email, username, isAdmin, userid
        """
        user_tuple = (firstname, lastname, othername, username,
                      hashed_password, email, phoneNumber)
        response = QuestionerDb.add_to_db(user_query, user_tuple)
        return response

    def check_for_admin(self, email):
        """Method to check for an Admin"""
        admin_query = """SELECT isAdmin, email FROM  users
                        WHERE email = '{}'""".format(email)
        response = QuestionerDb.retrieve_one(admin_query)
        if response['isadmin'] is True:
            return response

    def get_user_by_email(self, email):
        user_email_query = """SELECT * FROM users WHERE email = '{}'""".format(
            email)
        user_response = QuestionerDb.retrieve_one(user_email_query)
        if not user_response:
            return False
        return user_response

    def validate_password(self, userpassword, user_email):
        query = """SELECT userpassword FROM users WHERE email='{}'""".format(
            user_email)
        result = QuestionerDb.retrieve_one(query)

        if not check_password_hash(result['userpassword'], userpassword):
            return False
        return True

    def generate_token(self, email, is_admin):
        """Method to generate token"""
        try:
            print("Which email am I?", email)
            payload = {
                'exp': datetime.utcnow() + timedelta(minutes=60),
                'iat': datetime.utcnow(),
                'email': email,
                'is_admin': is_admin
            }
            token = jwt.encode(
                payload,
                str(current_app.config.get('SECRET')),
                algorithm='HS256'
            )
            return token
        except Exception as error:
            return str(error)

    @staticmethod
    def decode_token(token):
        '''Method for decoding token generated'''
        token_payload = jwt.decode(token, str(
            current_app.config.get('SECRET')), algorithms=['HS256'])
        return token_payload

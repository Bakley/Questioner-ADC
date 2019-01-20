import os
import jwt
from datetime import datetime, timedelta
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

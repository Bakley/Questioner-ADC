import os
from datetime import datetime, timedelta
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

from app.api.v2.dbmodel import QuestionerDb

class UserModels:
    """User class models"""
    
    # def __init__(self, *args, **kwargs):
    #     """Initialize the user"""
    #     self.firstname = firstname
    #     self.lastname = lastname
    #     self.othername = othername
    #     self.username = username
    #     self.userpassword = userpassword
    #     self.email = email
    #     self.phonenumber = phonenumber 
    #     self.registered = datetime.now()
    #     self.isAdmin = FALSE

    def create_a_user(self, email):
        query = """INSERT INTO users(firstname, lastname, username, userpassword, email, phonenumber, isAdmin) VALUES (%s,) RETURNING id, email, isAdmin;"""
        record_to_insert = (email)
        response = QuestionerDb.add_to_db(query, record_to_insert)
        return response

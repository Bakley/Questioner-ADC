import os
import psycopg2
from flask import current_app
from psycopg2.extras import RealDictCursor
from app.api.v2 import sql_scripts


class QuestionerDb:
    """Class to create the database"""

    @classmethod
    def start_db(cls, uri):
        """
        method to initialize the database
        """
        cls.conn = psycopg2.connect(uri)
        cls.cur = cls.conn.cursor(cursor_factory=RealDictCursor)

    @classmethod
    def create_tables(cls):
        scripts = [
            sql_scripts.create_tbl_users,
            sql_scripts.create_tbl_meetups,
            sql_scripts.create_tbl_questions
            ]

        try:

            for query in scripts:
                cls.cur.execute(query)
                cls.conn.commit()

            return "Tables successfully created"
        except BaseException:
            return "Failed to create a tables"
    @classmethod
    def insert_default_data(cls):
        query = sql_scripts.query_insert_admin
        cls.cur.execute(query)

    @classmethod
    def destroy(cls):
        query1 = """DROP TABLE users, meetups, questions;"""
        cls.cur.execute(query1)

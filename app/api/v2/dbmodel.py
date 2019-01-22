import os
import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash


class QuestionerDb:
    """Creates connection to the database and creates tables"""
    @classmethod
    def init_db(cls, uri):
        """
        method to initialize the database
        """
        cls.conn = psycopg2.connect(uri)
        cls.cur = cls.conn.cursor(cursor_factory=RealDictCursor)
        print("Database = ", cls.conn.get_dsn_parameters(), "\n")

    @classmethod
    def build_all(cls):
        """
        method that creates the tables in the database
        """
        try:
            cls.cur.execute("""
            CREATE TABLE IF NOT EXISTS users(
            userId serial PRIMARY KEY,
            firstname VARCHAR NOT NULL,
            lastname VARCHAR NOT NULL,
            othername VARCHAR NULL,
            username VARCHAR NOT NULL,
            userpassword VARCHAR NOT NULL,
            email VARCHAR UNIQUE NOT NULL,
            phonenumber INTEGER NOT NULL,
            registered TIMESTAMP default current_timestamp,
            isAdmin BOOLEAN DEFAULT FALSE
            );
            CREATE TABLE IF NOT EXISTS meetups(
            meetupId serial PRIMARY KEY,
            userId  INTEGER NOT NULL,
            location VARCHAR NOT NULL,
            topic VARCHAR NOT NULL,
            tags TEXT [] NOT NULL,
            images VARCHAR [],
            createdOn TIMESTAMP default current_timestamp,
            happeningOn TIMESTAMP NOT NULL,
            FOREIGN KEY (userId) REFERENCES users (userId) ON DELETE CASCADE
            );
            CREATE TABLE IF NOT EXISTS questions(
            questionid serial PRIMARY KEY,
            userId INTEGER NOT NULL,
            meetupId INTEGER NOT NULL,
            title VARCHAR NOT NULL,
            body VARCHAR NOT NULL,
            votes INTEGER NOT NULL,
            createdOn TIMESTAMP NOT NULL,
            FOREIGN KEY (meetupId) REFERENCES meetups (meetupId) ON DELETE CASCADE,
            FOREIGN KEY (userId) REFERENCES users (userId) ON DELETE CASCADE
            );
            CREATE TABLE IF NOT EXISTS rsvps(
            rsvpId serial PRIMARY KEY NOT NULL,
            meetup INTEGER NOT NULL,
            FOREIGN KEY (meetup) REFERENCES meetups(meetupId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            createdBy integer REFERENCES users(userId),
            response varchar (5)
            );
            CREATE TABLE IF NOT EXISTS comments(
            commentId serial PRIMARY KEY NOT NULL,
            question INTEGER NOT NULL,
            title varchar NOT NULL,
            body varchar NOT NULL,
            FOREIGN KEY (question) REFERENCES questions(questionId)\
            ON UPDATE CASCADE ON DELETE CASCADE,
            comment varchar NOT NULL
            );
            """
                            )
            cls.conn.commit()
            QuestionerDb.persist_to_db_admin()
            print("Table created successfully in PostgreSQL ")
        except (Exception, psycopg2.Error) as e:
            print("on db = ", e)

    @classmethod
    def persist_to_db_admin(cls):
        """
        method that saves Admin queries into the database
        """
        try:
            username = "Admin"
            query = """SELECT * FROM
            users WHERE username = '{}'""".format(username)
            cls.cursor.execute(query)
            admin = cls.cursor.fetchone()
            if not admin:
                query_insert_admin = """INSERT INTO
                users (firstname, lastname, othername, username,
                userpassword, email, phonenumber,
                isAdmin)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING userid, email, username, isAdmin;"""
                hashed_password = generate_password_hash("Admin@254")
                tuple_data = ('superuser', 'superadmin', 'Broadminded',
                              'Admin', '{}', 'super@admin.org', '0703912965',
                              'TRUE').format(hashed_password)
                cls.cur.execute(query_insert_admin, tuple_data)
                cls.conn.commit()
                print("Admin added!")
        except Exception as e:
            print(e.pgerror)

    @classmethod
    def add_to_db(cls, query_string, tuple_data):
        """
        method that saves queries into the database
        """
        try:
            cls.cur.execute(query_string, tuple_data)
            cls.conn.commit()
            response = cls.cur.fetchall()
            return response
        except Exception as e:
            print(e.pgerror)

    @classmethod
    def persist_to_db(cls, query_string, tuple_data):
        """
        method that saves queries into the database
        """
        try:
            cls.cur.execute(query_string, tuple_data)
            cls.conn.commit()
        except Exception as e:
            print(e.pgerror)

    @classmethod
    def check_email(cls, query_string, tuple_data):
        """
        method that saves queries into the database
        """
        cls.cur.execute(query_string, tuple_data)
        return cls.cur.fetchone()

    @classmethod
    def retrieve_one(cls, query_string):
        """
        method returns data on a particular row from the database
        """
        cls.cur.execute(query_string)
        return cls.cur.fetchone()

    @classmethod
    def retrieve_all(cls, query_string):
        """
        returns all specified columns from table rows
        """
        cls.cur.execute(query_string)
        return cls.cur.fetchall()

    @classmethod
    def update_row(cls, query_string):
        """
        method that sends an update query to the database
        """
        resp = cls.cur.execute(query_string)
        cls.conn.commit()
        return resp

    @classmethod
    def drop_all(cls):
        """
        Destroys tables form the database
        """
        cls.cur.execute(
            """DROP TABLE IF EXISTS users, meetups, questions, rsvps, comments CASCADE;""")
        cls.conn.commit()

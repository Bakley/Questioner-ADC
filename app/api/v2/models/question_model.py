"""Question CRUD functionality"""
from app.api.v2.dbmodel import QuestionerDb


class QuestionModel:
    """Questions class model"""

    def create_a_question(self, title, body, userId, meetupId):
        """Method to create a meetup"""
        question_query = """INSERT INTO
        questions (title, body, userId, meetupId)
        VALUES(%s, %s, %s, %s)
        RETURNING title, body, userId, meetupId
        """

        question_tuple = (title, body, userId, meetupId)
        response = QuestionerDb.add_to_db(question_query, question_tuple)
        return response

    def upvote_question(self, id):
        """User can upvote"""
        upvote_query = """UPDATE questions
        SET votes = votes + 1
        WHERE questionid = '{}'""".format(id)
        QuestionerDb.update_row(upvote_query)
        fetch_query = """SELECT * FROM questions
        WHERE questionid = '{}'""".format(id)
        response = QuestionerDb.retrieve_all(fetch_query)
        if not response:
            return False
        payload = {
            "question": response
        }
        return payload

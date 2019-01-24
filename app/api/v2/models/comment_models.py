"""Comment CRUD functionality"""
from app.api.v2.dbmodel import QuestionerDb


class CommentModel:
    """Comment class model"""

    def create_comment(self, question, comment):
        """Method to create a comment"""
        comment_query = """INSERT INTO comments
        (question, comment)
        VALUES (%s, %s)
        RETURNING question, comment"""
        comment_tuple = (question, comment)
        response = QuestionerDb.add_to_db(comment_query, comment_tuple)
        return response

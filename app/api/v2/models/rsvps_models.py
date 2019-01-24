"""RSVPS CRUD functionality"""
from app.api.v2.dbmodel import QuestionerDb


class RsvpsModel:
    """Rspvs class model"""

    def create_a_rspvs(self, meetupId, response, createdBy):
        """Method to save rspv records"""
        rspv_query = """INSERT INTO
        rsvps (meetup, response, createdBy)
        VALUES (%s, %s, %s)
        RETURNING meetup, response, createdBy
        """
        rspv_tuple = (meetupId, response, createdBy)
        response = QuestionerDb.add_to_db(rspv_query, rspv_tuple)
        return response

    def get_a_specific_rspvs(self, id):
        """Get one rspvs by id"""

        fetch_query = """SELECT * FROM
        rsvps WHERE rsvpId={}""".format(id)
        response = QuestionerDb.retrieve_all(fetch_query)
        if not response:
            return False
        payload = {
            "one_rspvs": response
        }
        return payload

"""Meetup CRUD functionality"""
from app.api.v2.dbmodel import QuestionerDb


class MeetupsModel:
    """CRUD functionality for the model"""

    def create_meetup(self, userid, location, topic, tags, happeningon):
        """Method to create a model record"""
        payload = {
            "userid": userid,
            "topic": topic,
            "location": location,
            "tags": tags,
            "happeningon": happeningon

        }
        meetup_query = """INSERT INTO
                        meetups (userid, location, topic, tags, happeningon)
                        VALUES (%s, %s, %s, %(date)s)
                        """

        meetup_tuple = (userid, location, topic, tags, happeningon)
        QuestionerDb.persist_to_db(meetup_query, meetup_tuple)
        return payload

    def get_a_specific_meetup(self, id):
        """Get one meetup by id"""

        fetch_query = """SELECT * FROM meetups WHERE meetupId={}""".format(
            id)
        response = QuestionerDb.retrieve_all(fetch_query)
        if not response:
            return False
        payload = {
            "one_meetup": response
        }
        return payload

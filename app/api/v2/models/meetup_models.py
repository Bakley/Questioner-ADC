"""Meetup CRUD functionality"""
import datetime
from app.api.v2.dbmodel import QuestionerDb


class MeetupsModel:
    """CRUD functionality for the model"""

    def create_meetup(self, location, topic, tags):
        """Method to create a model record"""
        meetup_query = """INSERT INTO
                        meetups (location, topic, tags)
                        VALUES (%s, %s, %s)
                        RETURNING meetupId, location, topic, tags
                        """

        meetup_tuple = (location, topic, tags)
        print("Tuple", meetup_tuple)
        res = QuestionerDb.add_to_db(meetup_query, meetup_tuple)
        print("Meetup response", res)
        return res

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

    def get_all_meetups(self):
        """Get all upcoming meetups"""

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        upcoming_query = """SELECT meetupId, topic, location, happeningOn, tags
         FROM meetups WHERE happeningOn > '{}'""".format(
            current_time)
        response = QuestionerDb.retrieve_all(upcoming_query)
        if not response:
            return False
        payload = {
            "upcoming_meetup": response
        }
        return payload

    def delete_a_specific_meetup(self, id):
        """Admin can delete a meetup"""
        fetch_query_for_delete = """SELECT * FROM meetups
        WHERE meetupId={}""".format(id)
        response = QuestionerDb.retrieve_one(fetch_query_for_delete)
        print("Delete this", response)
        if not response:
            return False
        delete_query = """DELETE FROM meetups WHERE meetupid={};""".format(id)
        QuestionerDb.deletion(delete_query)

"""Meetup models"""

from datetime import datetime

questions = []


class QuestionsModel:
    """Meetup class models"""

    def __init__(self):
        """Initializes the model"""
        self.db = questions

    def create_meetup(self, body, title, tags):
        """Method to save meetup records"""
        payload = {
            "id": len(self.db) + 1,
            "body": body,
            "title": title,
            "votes": 0,
            "createdOn": datetime.utcnow().isoformat()
        }
        self.db.append(payload)
        return payload

    def get_all_questions(self):
        """Retrieves all upcoming meetups"""
        return self.db

    def get_a_specific_question(self, id):
        """Retrieves a specific meetup"""
        meetup = [new_meetup for new_meetup in self.db
                  if new_meetup["id"] == id]
        return meetup

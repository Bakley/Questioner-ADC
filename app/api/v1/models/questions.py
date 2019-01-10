"""Meetup models"""
from app.api.v1.models.meetups import meetup_models
from datetime import datetime

questions = []


class QuestionsModel:
    """Meetup class models"""

    def __init__(self):
        """Initializes the model"""
        self.db = questions

    def create_question(self, body, title, meetup, createdBy):
        """Method to save question records"""

        payload = {
            "id": len(self.db) + 1,
            "body": body,
            "title": title,
            "votes": 0,
            "meetup": meetup,
            "createdBy": createdBy,
            "createdOn": datetime.utcnow().isoformat()
        }
        self.db.append(payload)
        return payload

    def get_all_questions(self):
        """Retrieves all upcoming meetups"""
        return self.db

    def get_a_specific_question(self, id):
        """Retrieves a specific meetup"""
        question = [new_question for new_question in self.db
                    if new_question["id"] == id]
        return question

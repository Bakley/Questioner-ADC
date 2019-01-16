"""Question models"""
from datetime import datetime

questions = []


class QuestionsModel:
    """Question class models"""

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

        return [
            {
                "user": payload["id"],
                "meetup": payload["meetup"],
                "title": payload["title"],
                "body": payload["body"],
                "votes": payload["votes"]
            }
        ]

    def get_all_questions(self):
        """Retrieves all upcoming meetups"""
        return self.db

    def get_a_specific_question(self, id):
        """Retrieves a specific meetup"""
        question = [new_question for new_question in self.db
                    if new_question["id"] == id]
        return question

    def upvote_question(self, id):
        """Increment vote by 1"""

        payload = [payload for payload in self.db if payload['id'] == id]

        if not payload:
            return False

        upvote_votes = self.db[0]["votes"] + 1
        self.db[0]["votes"] = upvote_votes

        if self.db:
            return [{
                "meetup": self.db[0]["meetup"],
                "title": self.db[0]["title"],
                "body": self.db[0]["body"],
                "votes": self.db[0]["votes"]
            }]

    def downvote_question(self, id):
        """Decrement vote by 1"""

        payload = [payload for payload in self.db if payload['id'] == id]

        if not payload:
            return False

        downvote_votes = self.db[0]["votes"] - 1

        self.db[0]["votes"] = downvote_votes

        if self.db:
            return [{
                "meetup": self.db[0]["meetup"],
                "title": self.db[0]["title"],
                "body": self.db[0]["body"],
                "votes": self.db[0]["votes"]
            }]

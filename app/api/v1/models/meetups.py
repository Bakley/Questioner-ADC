"""Meetup models"""

from datetime import datetime

meetups = []


class MeetupsModel:
    """Meetup class models"""

    def __init__(self):
        """Initializes the model"""
        self.db = meetups

    def create_meetup(self, location, topic, tags):
        """Method to save meetup records"""
        payload = {
            "id": len(self.db) + 1,
            "location": location,
            "topic": topic,
            "tags": tags,
            "createdOn": datetime.utcnow().isoformat(),
            "happeningOn": datetime.utcnow().isoformat()
        }
        self.db.append(payload)
        return payload

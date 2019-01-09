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

    def get_all_meetups(self):
        """Retrieves all upcoming meetups"""
        return self.db

    def get_a_specific_meetup(self, id):
        """Retrieves a specific meetup"""
        meetup = [new_meetup for new_meetup in self.db
                  if new_meetup["id"] == id]
        return meetup

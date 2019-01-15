"""Meetup models"""

from datetime import datetime

meetup_models = []


class MeetupsModel:
    """Meetup class models"""

    def __init__(self):
        """Initializes the model"""
        self.db = meetup_models

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
        return [{
            "topic": payload["topic"],
            "location": payload["location"],
            "happeningOn": payload["happeningOn"],
            "tags": payload["tags"]
        }]

    def get_all_meetups(self):
        """Retrieves all upcoming meetups"""
        return self.db

    def get_a_specific_meetup(self, id):
        """Retrieves a specific meetup"""
        meetup = [new_meetup for new_meetup in self.db
                  if new_meetup["id"] == id]
        if not meetup:
            return False
        return [{
            "id": meetup[0]["id"],
            "topic": meetup[0]["topic"],
            "location": meetup[0]["location"],
            "happeningOn": meetup[0]["happeningOn"],
            "tags": meetup[0]["tags"]
        }]

    def get_a_meetup_by_loaction(self, location):
        """Retrieves a meetup by its location"""
        meetup_location = [new_meetup for new_meetup in self.db
                           if new_meetup["location"] == location]
        if meetup_location:
            return True
        return False

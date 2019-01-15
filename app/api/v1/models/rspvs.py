from app.api.v1.models.meetups import meetup_models
rspv_models = []


class RspvsModel:
    """rspv class models"""

    def __init__(self):
        """Initializes the model"""
        self.db = rspv_models

    def create_rspv(self, topic, status, createdBy):
        """Method to save rspv records"""

        meetup = [new_meetup['id'] for new_meetup in meetup_models]
        if not meetup:
            return False
        print(meetup)
        payload = {
            "id": len(self.db) + 1,
            "meetup": meetup[0],
            "topic": topic,
            "status": status,
            "createdBy": createdBy
        }
        self.db.append(payload)
        return payload

    def get_all_rspvs(self):
        """Retrieves all upcoming rspvs"""
        return self.db

    def get_a_specific_rspv(self, id):
        """Retrieves a specific rspv"""
        rspv = [new_rspv for new_rspv in self.db
                if new_rspv["id"] == id]
        return rspv

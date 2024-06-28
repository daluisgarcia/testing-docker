from core.database import get_database

db = get_database()

class Greetings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable=False)

    def as_dict(self):
        return {
            "id": self.id,
            "message": self.message
        }

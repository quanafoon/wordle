from App.database import db

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, id):
        self.id = id

    def get_json(self):
        return{
            'id': self.id,
        }


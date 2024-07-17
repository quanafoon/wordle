from App.database import db

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), nullable=False)
    
    def __init__(self, code):
        self.code = code

    def get_json(self):
        return{
            'id': self.id,
            'code': self.code
        }


from App.database import db

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), nullable=False)
    word = db.Column(db.String(5))
    
    def __init__(self, code, word):
        self.code = code
        self.word = word

    def get_json(self):
        return{
            'id': self.id,
            'code': self.code,
            'word': self.word
        }


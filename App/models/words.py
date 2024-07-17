from App.database import db

class Words(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(5), nullable=False)
    
    def __init__(self, word):
        self.word = word

    def get_json(self):
        return{
            'id': self.id,
            'code': self.word
        }
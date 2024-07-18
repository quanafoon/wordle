from App.database import db

class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), nullable=False)
    ready = db.Column(db.Boolean, nullable=False)
    
    def __init__(self, code, ready):
        self.code = code
        self.ready = ready

    def get_json(self):
        return{
            'id': self.id,
            'code': self.code,
            'ready': self.ready
        }


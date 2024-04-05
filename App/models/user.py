from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    guess = db.relationship('UserGuess', backref='User', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
    
    # The User Clicks The Start Button And Initiates A Game
    def start_game():
        pass

    # The User Finalizes A Guess By Pressing Enter Or The "Check" Button 
    def guess_puzzle(guess):
        pass

    # The User Forfeits
    def give_up():
        pass

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

class UserGuess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    guess = db.Column(db.String(10), nullable=False)

    def get_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'guess': self.guess
        }
    
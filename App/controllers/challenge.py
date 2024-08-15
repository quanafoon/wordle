from App.models import Challenge, Words
from App.database import db
import random
import string


def get_word():
    num = random.randint(1,250)
    word = Words.query.filter_by(id=num).first()
    return word.word

def createChallenge(code):
    
    word= get_word()
    new_challenge = Challenge(code=code, word=word, playing=1)
    if new_challenge:
        db.session.add(new_challenge)
        db.session.commit()
        return new_challenge
    else:
        return None

def addPlayer(code):
    challenge = Challenge.query.filter_by(code=code).first()
    challenge.playing += 1
    db.session.commit()
    return challenge

def removePlayer(code):
    challenge = Challenge.query.filter_by(code=code).first()
    challenge.playing -= 1
    db.session.commit()
    return challenge

def check(code):
    challenge = Challenge.query.filter_by(code=code).first()
    if challenge.playing == 0:
        db.session.delete(challenge)
        db.session.commit()
    
def joinChallenge(code):
    challenge = Challenge.query.filter_by(code=code).first()
    if challenge:
        playing = challenge.playing
        
        return challenge
    else:
        return None

def get_code(id):
    challenge = Challenge.query.filter_by(id=id).first()
    if challenge:
        return challenge.code
    return None

def get_challenge(id):
    challenge = Challenge.query.filter_by(id=id).first()
    if challenge:
        return challenge
    return None

def get_challengeID(code):
    challenge = Challenge.query.filter_by(code=code).first()
    if challenge:
        return challenge.id
    return None

def get_ch_by_code(code):
    challenge = Challenge.query.filter_by(code=code).first()
    if challenge:
        return challenge
    return None

def get_code(id):
    challenge = Challenge.query.filter_by(id=id).first()
    if challenge:
        return challenge.code
    return None

def get_challenges():
    challenges = Challenge.query.all()
    return [challenge.get_json() for challenge in challenges]

def cancel_challenge(challenge_id):
    challenge = Challenge.query.get(challenge_id)
    if challenge:
        db.session.delete(challenge)
        db.session.commit()
        return challenge
    else:
        return None

def is_valid(code):
    valid = Challenge.query.filter_by(code=code)
    if valid:
        return valid
    else:
        return None


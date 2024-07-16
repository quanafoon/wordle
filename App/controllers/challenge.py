from App.models import Challenge
from App.database import db
import random
import string

def createChallenge(code):
    new_challenge = Challenge(code=code)
    if new_challenge:
        db.session.add(new_challenge)
        db.session.commit()
        return new_challenge
    else:
        return None

def get_code(id):
    challenge = Challenge.query.filter_by(id=id).first()
    if challenge:
        return Challenge.code
    return None

def get_challenge(id):
    challenge = Challenge.query.filter_by(id=id).first()
    if challenge:
        return Challenge
    return None

def get_challengeID(code):
    challenge = Challenge.query.filter_by(id=id).first()
    if challenge:
        return Challenge.id
    return None
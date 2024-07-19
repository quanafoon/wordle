from App.models import Challenge
from App.database import db
import random
import string

def createChallenge(code):
    new_challenge = Challenge(code=code, ready=False)
    if new_challenge:
        db.session.add(new_challenge)
        db.session.commit()
        return new_challenge
    else:
        return None

def joinChallenge(code):
    challenge = Challenge.query.filter_by(code=code).first()
    if challenge:
        challenge.ready = True
        db.session.commit()
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
from App.models import Challenge
from App.database import db
import random
import string

def generateID(length=4):
    letters_and_digits = string.ascii_letters + string.digits
    challengeID =  ''.join(random.choice(letters_and_digits) for i in range(length))
    #db.session.add(challengeID)
    return challengeID
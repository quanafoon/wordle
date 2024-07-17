from .user import create_user
from .words import load_words
from App.database import db
import csv


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    load_words()
    
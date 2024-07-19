from App.models import Words
from App.database import db
import csv
import random

def load_words():
    with open('words.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)  
        header = next(csvreader)

        for row in csvreader: 
            id = row[0]
            word = row[1]
            
            word = Words(
                word = word
            )
            db.session.add(word)
        db.session.commit()

def get_words():
    words = Words.query.all()
    return [word.get_json() for word in words]


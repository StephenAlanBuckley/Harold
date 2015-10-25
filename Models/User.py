from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    person_id = db.Column(db.Integer)

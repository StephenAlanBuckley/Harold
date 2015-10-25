from database import db

class User(db.Model):
    id = db.Column(db.integer, primary_key = true)
    person_id = db.Column(db.Integer)

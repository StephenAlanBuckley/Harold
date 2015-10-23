import datetime
from BaseModel import BaseModel
from server import db

class Person(BaseModel, db.Model):
    __tablename__ = __name__
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

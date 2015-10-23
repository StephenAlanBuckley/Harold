import datetime
from BaseModel import BaseModel
from Models.Team.Member import Team_Member
from server import db

class Team(BaseModel, db.Model):
    __tablename__ = __name__
    id = db.Column(db.integer, primary_key = true)
    name =  db.Column(db.String(200))
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


    def __init__(self):
        self.members = getMembers()
    #/__init__

    def __repr__(self):
        return self.name
    #/__repr__

    def getMembers():
        members = Team_Member.query.filter(Team_Member.team_id == self.id)
        return members
    #/getMembers

#/Team

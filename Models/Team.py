import datetime
from BaseModel import BaseModel
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

#    def getMembers():
#        members = Team_Member.query.filter(Team_Member.team_id == self.id)
#        return members
#    #/getMembers

#/Team


#class Team_Member(BaseModel, db.Model):
#    __tablename__ = __name__
#    id = db.Column(db.integer, primary_key = true)
#    team_id = db.Column(db.integer)
#    person_id = db.Column(db.integer)
#    status = db.Column(db.String(200))
#    create_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
#    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
#
#    def __init__(self, team_id, person_id, status):
#        self.team_id = team_id
#        self.person_id = person_id
#        self.status = status
#    #/__init__
#
#/Member

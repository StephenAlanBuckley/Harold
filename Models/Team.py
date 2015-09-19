class Team(Database.Model):
    id = Database.Column(Database.integer, primary_key = true)
    name =  Database.Column(Database.String(200))
    create_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)


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

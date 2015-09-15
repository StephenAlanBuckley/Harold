class Team_Member(Database.Model):
    id = Database.Column(Database.integer, primary_key = true)
    team_id = Database.Column(Database.integer)
    person_id = Database.Column(Database.integer)
    status = Database.Column(Database.String(200))
    create_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, team_id, person_id, status):
        self.team_id = team_id
        self.person_id = person_id
        self.status = status
    #/__init__

#/Member

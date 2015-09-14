class Team(Database.Model):
    id = Database.Column(Database.Integer, primary_key = True)
    name =  Database.Column(Database.String(200))

    members[]

    def __init__(self, id, name):
        self.id = id
        self.name = name
    #/__init__

    def __repr__(self):
        return self.name
    #/__repr__

#/Team

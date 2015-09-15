class Actor(Database.Model):
    id = Database.Column(Database.integer, primary_key = true)
    team_id = Database.Column(Database.integer)
    person_id = Database.Column(Database.integer)
    create_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

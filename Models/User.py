class User(Database.Model):
    id = Database.Column(Database.integer, primary_key = true)
    person_id = Database.Column(Database.Integer)

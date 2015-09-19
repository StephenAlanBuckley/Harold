class Person(BaseModel):
    id = Database.Column(Database.integer, primary_key = true)
    name = Database.Column(Database.String(200))
    create_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

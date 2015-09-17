class Performer(Database.Model):
    id = Database.Column(Database.integer, primary_key = true)
    team_id = Database.Column(Database.integer)
    person_id = Database.Column(Database.integer)
    show_id = Database.Column(Database.integer)
    create_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def getPerformersInShow(show):
        results = Performer.query.filter(Performer.show_id = show.id)
        return results
    #/getPerformersInShow

    def getNumberOfTimesPersonHasPerformed(person):
        per = Performer.query.filter(Performer.person_id = person.id)
        return len(results)
    #/getPerformersInShow
#/Performer

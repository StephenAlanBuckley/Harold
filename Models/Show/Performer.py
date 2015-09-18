class Show_Performer(Database.Model):
    id = Database.Column(Database.integer, primary_key = true)
    team_id = Database.Column(Database.integer)
    person_id = Database.Column(Database.integer)
    show_id = Database.Column(Database.integer)
    create_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = Database.Column(Database.DateTime, nullable=False, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def __init__(self, team, person, show):
        self.team_id = team.id
        self.person_id = person.id
        self.show_id = show.id
    #/__init__

    def getPerformersInShow(show):
        results = Show_Performer.query.filter(Show_Performer.show_id = show.id)
        return results
    #/getPerformersInShow

    def getNumberOfTimesPersonHasPerformed(person):
        performances = Show_Performer.query.filter(Show_Performer.person_id = person.id)
        performance_count = len(performances)
        return performance_count
    #/getPerformersInShow

    def getLastTimeTeamPerformed(team):
        most_recent_performance = Show_Performer.query.order_by(Show_Performer.update_date).limit(1)
        return most_recent_performance.update_date
    #/getLastTimeTeamPerformed
#/Show_Performer

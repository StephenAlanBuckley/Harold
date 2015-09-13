class Team_Finder:
    db = None

    def __init__():
        self.db = Database()
    #/__init__

    def find(id):
        query_string = "SELECT * FROM team WHERE team_id=%s"
        params = [id]
        results = self.db->executeQuery(query_string, params)
        team = Team(results.id, results.name)
        return team
    #/find

#/Team_Finder

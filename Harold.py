from Models.Team import Team

class Harold:
  def __init__(self):
      self.Philosophy = "Frame, Heighten, Explore. Team First, Can't Lose!"
      self.Author = "Stephen Buckley"
      # =================================================================== #
      #                                HAROLD
      # =================================================================== #
      #          Improv Backend Butler For the Millenial In All Of Us
      # =================================================================== #
      #          Harold is the last member of every improv team. Harold
      #          helps keep you organized, reminds your team about
      #          upcoming shows, and keeps things chugging along nicely.
      # =================================================================== #
      self.logged_in = False
      self.user = None
  #/__init__

  def loginAsUser(login_id):
      self.user = User.query.filter(User.user_id == login_id)
      if self.user is not None:
          self.logged_in = True
      else:
          return False
      #/if
      return True
  #/loginAsUser

  def getMyUpcomingShows():
      if self.logged_in is False or self.user is None:
          return
      #/if

      now = time.time()
      all_my_performances = Show_Performer.query.filter(Show_Performer.person_id == self.user.person_id)
      upcoming_show_ids = []
      for my_performance in all_my_performances:
          my_show_id = my_performance.show_id
          my_show = Show.query.filter(Show.id == my_show_id)
          if my_show.time > now:
              upcoming_show_ids.append(my_show_id)
          #/if
      #/for
      return upcoming_show_ids
  #/getMyUpcomingImprovShows

  ######################################
  # Creates a team and returns its id  #
  ######################################
  def createNewTeam(name, second):
      my_team = Team()
      my_team.name = name
      my_team.save()
      return my_team.id
  #/createNewTeam

#/Harold

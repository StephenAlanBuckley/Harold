###########################################################################
# Made this base model as a wrapper and the regular SQLAlchemy db.Model.  #
# With this, python has stolen my heart forever. What a perfect ORM       #
###########################################################################


class BaseModel():
    #/ Saves the modified class to the Database
    def save():
        if db is not None:
            Database.session.add(self)
            Database.session.commit()
        #/if
    #/save
#/BaseModel

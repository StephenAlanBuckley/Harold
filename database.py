#This is to prevent dependency issues when two files both need
#to import the db but can't be circularly dependent
#
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

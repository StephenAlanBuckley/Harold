import os
import psycopg2
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
dev_connect_string = "postgresql://localhost/sbuckley"
#/ app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = dev_connect_string
# Gotta figure out how to have Config objects at some point
#/ app.config.from_object(os.environ['APP_SETTINGS'])
#/ print(os.environ['APP_SETTINGS'])

Database = SQLAlchemy(app)
@app.route('/')
def Harold_Homepage(args):
    return "Hello! I'm Harold."

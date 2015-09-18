import os
import psycopg2
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
Database = SQLAlchemy(app)

@app.route('/')
def Harold_Homepage():
    return "Hello, I'm Harold"

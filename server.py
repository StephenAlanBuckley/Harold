import os
import psycopg2
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])
Database = SQLAlchemy(app)

@app.route('/')
def Harold_Homepage():
      return "hi"

if __name__ == "__main__":
      app.run()

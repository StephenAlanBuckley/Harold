import os
import psycopg2
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import Models.Team

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


@app.route('/')
def Harold_Homepage():
    return "wow"

if __name__ == "__main__":
      port = int(os.environ.get('PORT', 5000))
      app.run(host='0.0.0.0', port=port)

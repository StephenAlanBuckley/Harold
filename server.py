import os
import psycopg2
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# Gotta figure out how to have Config objects at some point
#/ app.config.from_object(os.environ['APP_SETTINGS'])
#/ print(os.environ['APP_SETTINGS'])

Database = SQLAlchemy(app)
@app.route('/')
def Harold_Homepage(environ, start_response):
      data = "Hello, World!\n"
      start_response("200 OK", [
          ("Content-Type", "text/plain"),
          ("Content-Length", str(len(data)))
      ])
      return iter([data])

if __name__ == "__main__":
      app.run(host='0.0.0.0')

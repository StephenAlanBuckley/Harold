import os
import psycopg2
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from Harold import Harold

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def Harold_Homepage():
    har = Harold();
    return "<strong>Did It</strong>"

if __name__ == "__main__":
      port = int(os.environ.get('PORT', 5000))
      app.run(host='0.0.0.0', port=port)

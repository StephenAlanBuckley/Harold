import os
import psycopg2
import urlparse

class Database:
    url
    conn = false

    def __init__():
        urlparse.uses_netloc.append("postgres")
        self.url = urlparse.urlparse(os.environ["DATABASE_URL"])

        conn = psycopg2.connect(
            database = self.url.path[1:],
            user = self.url.username,
            password = self.url.password,
            host = self.url.hostname,
            port =self.url.port
        )
    #/__init__

    def executeQuery(query, params):
        if self.conn is false:
            return false
        #}
        query_cursor = self.conn.cursor()
        result = query_cursor.execute(query, params)
    #/executeQuery

#/Database

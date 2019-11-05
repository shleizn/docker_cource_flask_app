from flask import Flask
from flaskext.mysql import MySQL
import pymysql
import time


app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'Flask'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Fpass'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
mysql.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/mysql')
def mysql_version():
    query = 'select version()'
    cursor.execute(query)
    return str(cursor.fetchall())

def warm_up():
    print('Attempting to connect to MySQL')
    deadline = 60
    counter = 0
    conn = None
    while not conn and counter < deadline:
        try:
            conn = mysql.connect()
            print('Successfuly connected')
            return conn
        except (ConnectionRefusedError, pymysql.err.OperationalError) as err:
            print('...')
            counter += 1
            time.sleep(1)
    else:
        print('Connection timed out')
        raise SystemExit(1)

if __name__ == '__main__':
    conn = warm_up()
    cursor = conn.cursor()
    app.run(host='0.0.0.0')


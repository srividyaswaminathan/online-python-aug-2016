from flask import Flask, render_template
from mysql_connection_errors import MySQLConnector

app = Flask(__name__) 

sqlDB = MySQLConnector(app, 'world')

@app.route('/')
def index():
	print sqlDB.query_db("SELECT name FROM cities WHERE name LIKE 'Alm%'")
	return render_template('index.html')

app.run(debug=True)
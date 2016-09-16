from flask import Flask
app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 

from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# import the Connector function
from mysqlconnection import MySQLConnector
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'posts')


def add_post(data):
	sql = 'INSERT INTO posts (description, created_at, updated_at)' 
	sql += ' VALUES (:description, NOW(), NOW()); '
	query_data = { 'description': data}
	return mysql.query_db(sql, query_data)

def get_posts():
	sql = "select * from posts order by created_at"
	return mysql.query_db(sql)


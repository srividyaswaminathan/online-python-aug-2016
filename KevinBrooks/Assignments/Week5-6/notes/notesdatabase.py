from flask import Flask
app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 

from flask.ext.bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# import the Connector function
from mysqlconnection import MySQLConnector
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'notes')


def add_note(data):
	sql = 'INSERT INTO notes (title, created_at, updated_at)' 
	sql += ' VALUES (:title, NOW(), NOW()); '
	query_data = { 'title': data}
	return mysql.query_db(sql, query_data)

def get_notes():
	sql = "select id, title, IFNULL(description,'') as 'description', created_at, updated_at from notes order by created_at"
	return mysql.query_db(sql)

def update_note(note_id, note):
	sql = 'update notes set description = :note where id = :id' 
	query_data = { 'id': note_id, 'note' : note }
	return mysql.query_db(sql, query_data)

def delete_note(note_id):
	sql = 'delete from notes where id = :note_id' 
	query_data = { 'note_id': note_id}
	return mysql.query_db(sql, query_data)

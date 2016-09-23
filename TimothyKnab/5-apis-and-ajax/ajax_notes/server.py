from flask import Flask, render_template, request, redirect, jsonify # jsonify lets us send JSON back!
from datetime import datetime
# Import MySQLConnector class from mysqlconnection.py
from mysqlconnection import MySQLConnector

#CONSTANTS
app = Flask(__name__)
'''
Set variable 'mysql' to be an instance of the MySQLConnector class,
taking our entire application as the first argument and the database
name as the second argument.
'''
mysql = MySQLConnector(app, 'ajax_notes_assgn_db')

#ROUTES
@app.route('/')
def index():
	query = "SELECT * FROM notes"
	notes = mysql.query_db(query)
	return render_template('index.html', notes=notes)

@app.route('/notes/index_json')
def index_json():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    return jsonify(notes=notes)

@app.route('/create', methods=['POST'])
def create():
	note = request.form
	data = {'title' : note['title']}
	query = "INSERT INTO notes(title, created_at, updated_at) VALUES(:title, NOW(), NOW());"
	mysql.query_db(query,data)
	return_query = "SELECT * FROM notes;"
	notes = mysql.query_db(return_query)
	return render_template('/partials/notes.html', notes=notes)

@app.route('/<id>/update/description', methods=['POST'])
def updateDescription(id):
	note = request.form
	data = {
		'description' : note['description' + id],
		'id' : id
	}
	query = "UPDATE notes SET description=:description, updated_at=NOW() WHERE id=:id;"
	mysql.query_db(query,data)
	query_return = "SELECT * FROM notes"
	notes = mysql.query_db(query_return)
	return render_template('/partials/notes.html', notes=notes)

@app.route('/<id>/update/title', methods=['POST'])
def updateTitle(id):
	note = request.form
	data = {
		'title' : note['title' + id],
		'id' : id
	}
	query = "UPDATE notes SET title=:title, updated_at=NOW() WHERE id=:id;"
	mysql.query_db(query,data)
	query_return = "SELECT * FROM notes"
	notes = mysql.query_db(query_return)
	return render_template('/partials/notes.html', notes=notes)

@app.route('/<id>/delete', methods=['POST'])
def delete(id):
	data = {'id' : id}
	query = "DELETE FROM notes WHERE id= :id;"
	mysql.query_db(query,data)
	query_return = "SELECT * FROM notes"
	notes = mysql.query_db(query_return)
	return render_template('/partials/notes.html', notes=notes)

#RUN AND DEBUG
app.run(debug=True)

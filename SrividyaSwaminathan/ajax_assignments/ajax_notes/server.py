from flask import Flask, render_template, session, redirect, request, jsonify
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'ajax_notes')

queries = {
			"show": "SELECT * from notes",	
			"create": "INSERT INTO notes (title, description, created_at,updated_at) VALUES (:title, :description, NOW(), NOW())",
			"update": "UPDATE notes SET title= :title, description= :description WHERE id= :id",
			"delete": "DELETE FROM notes WHERE id= :id"
}

#functions
@app.route("/notes")
def index():	
	return render_template("index.html")


@app.route("/notes_partial")
def notes_partial():
	query = queries['show']
	all_posts = mysql.query_db(query)
	return render_template("partials/post.html", posts=all_posts)


@app.route("/notes/create", methods=["POST"])
def create_notes():
	query = queries['create']
	title = request.form['new_note_title']
	description = request.form['new_note_description']
	data = {
			 'title': title,
			 'description':	description
			}
	new_post = mysql.query_db(query, data)
	return notes_partial()

@app.route("/notes/edit/<id>", methods=["POST"])
def edit_notes(id):
	query = queries['update']
	title = request.form['heading']
	description = request.form['text']
	data = {
			'title': title,
			'description': description,
			'id': id
	}
	edit_notes = mysql.query_db(query, data)
	print "edited notes data", edit_notes
	#return redirect("/notes")
	return notes_partial()




@app.route("/notes/delete/<id>", methods=["POST"])
def delete_notes(id):
	query = queries['delete']
	data = {
			 'id': id
	}
	deleted_post = mysql.query_db(query, data)
	return notes_partial()

app.run(debug=True) 

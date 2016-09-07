from flask import Flask, render_template, request, redirect, flash
from dbconnection import MySQLConnector

app = Flask(__name__) 
app.secret_key = 'ThisIsSecret'
db = MySQLConnector(app, 'friendsdb')

queries = {
	'show_all': 'SELECT * FROM friends',
	'create': 'INSERT INTO friends(first_name, last_name, email, created_at, updated_at) VALUES(:first_name, :last_name, :email, NOW(), NOW())',
	'show': 'SELECT * FROM friends WHERE id = :id',
	'update': 'UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id',
	'delete': 'DELETE FROM friends WHERE id=:id'
}

@app.route('/')
def index():
	friends = db.query_db(queries['show_all'])
	return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	if (request.form['first_name'] and request.form['last_name'] and request.form['email']): 		
		data = { 
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email']
		}
		db.query_db(queries['create'], data)
		return redirect('/')
	else:
		flash('Invalid Entry', 'error')
		return redirect('/')

@app.route('/friends/<id>/edit', methods=['GET']) 
def show(id):
	data = {
		'id': id
	}
	friend = db.query_db(queries['show'], data) # This gets a list with one obj inside [{}]. 
	return render_template('edit.html', friend=friend[0])
	
@app.route('/friends/<id>', methods=['POST'])
def update(id):
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'email': request.form['email'],
		'id': id
	}
	db.query_db(queries['update'], data)
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def delete(id):
	data = {
		'id': id
	}
	db.query_db(queries['delete'], data)
	return redirect('/')

app.run(debug=True)
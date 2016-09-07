from flask import Flask, render_template, redirect, request, session, flash
from dbconnection import MySQLConnector
import re

app = Flask(__name__) 
app.secret_key = 'ThisIsSecret'

db = MySQLConnector(app, 'emailsdb')
email_regex = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

queries = {
	'create_new': 'INSERT INTO emails(address, created_at, updated_at) VALUES(:address, NOW(), NOW())',
	'get_all': 'SELECT * FROM emails',
	'get_address': 'SELECT address FROM emails WHERE address = :address',
	'get_date': 'SELECT created_at FROM emails WHERE address = :address',
	'delete_id': 'DELETE FROM emails WHERE id = :id',
	'delete_address': 'DELETE FROM emails WHERE address = :address'
}

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success')
def show():
	all_emails = db.query_db('SELECT * FROM emails')
	return render_template('success.html', all_emails=all_emails)

@app.route('/success', methods=['post'])
def process():
	if email_regex.match(request.form['email']): 
		data = { 'address': request.form['email'] }
		list = db.query_db(queries['get_address'], data)
		if (list == []): # Check for duplicates -- Will return a blank list [] if there is no duplicate.
			db.query_db(queries['create_new'], data) # Store new email the db.
			newest_email = db.query_db(queries['get_address'], data) # Get the newest entry to display in green in success.html.
			date = db.query_db(queries['get_date'], data)
			all_emails = db.query_db(queries['get_all'])
			total = len(all_emails)
			return render_template('success.html', all_emails=all_emails, new_entry=newest_email[0], date=date, total=total)
		else: # Else it already exists. Flash error. 
			flash('Email already registered.', 'error')
			return redirect('/')
		
	else: # Else it's not valid. 
		flash('Email not valid', 'error') 
		return redirect('/')


@app.route('/<id>', methods=['post'])
def eraseIt(id):
	data = { 'id': id}
	db.query_db(queries['delete_id'], data)
	return redirect('/success')


@app.route('/delete', methods=['post'])
def delete():
	if email_regex.match(request.form['delete']):
		data = { 'address': request.form['delete']} 
		db.query_db(queries['delete_address'], data)
	else:
		flash('Invalid Email/id. Nothing to delete.', 'error')
	return redirect('/success')

app.run(debug=True)
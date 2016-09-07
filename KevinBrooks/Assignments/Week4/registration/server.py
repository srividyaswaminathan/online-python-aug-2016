from flask import Flask, render_template, request, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

from flask.ext.bcrypt import Bcrypt

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PWD_REGEX_UPPER = re.compile(r'[A-Z]')
PWD_REGEX_LOWER = re.compile(r'[a-z]')

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'users')

bcrypt = Bcrypt(app)

@app.route('/', methods=['get'])
def index():
	return render_template('index.html', message_display='none')

@app.route('/register', methods=['post'])
def register():
	session['first'] = request.form['first']
	session['last'] = request.form['last']
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	session['confirm_password'] = request.form['confirm_password']
	if not validate_all():
		return render_template('index.html', message_display='block', first=session['first'], last=session['last'], email=session['email'])
	else:
		add_user()
		return redirect('/users')

	return render_template('index.html')

@app.route('/users', methods=['get'])
def login():
	sql = 'SELECT * FROM users WHERE email=:email LIMIT 1'
	query_data = {'email' : session['email']}
	
	record = mysql.query_db(sql, query_data)
	pw_hash = record[0]['password']
	
	sql = "SELECT first_name, last_name, email FROM users WHERE 1=0"
	if bcrypt.check_password_hash(pw_hash, session['password']):
		print ('logged in')	
		sql = "SELECT  first_name, last_name, email FROM users ORDER BY first_name, last_name"
		login = 'signed in'
	else:
		print ('not logged in')
		login = 'not signed in'

	records = mysql.query_db(sql)
		
	return render_template('users.html', login_verb=login, records=records)


def validate_all():
	ret = True
	ret = validate_text() & ret
	ret = validate_email() & ret
	ret = validate_password() & ret
	return ret

def validate_text():
	errors = []
	if len(session['first'].strip()) < 1:
		errors.append('First cannot be blank.')
	if len(session['last'].strip()) < 1:
		errors.append('Last cannot be blank.')
	if len(session['email'].strip()) < 1:
		errors.append('Email cannot be blank.')
	if len(session['password'].strip()) < 1:
		errors.append('Password cannot be blank.')

	if len(errors) > 0:
		for msg in errors:
			flash(msg)
		return False

	return True

def validate_email():
	if not EMAIL_REGEX.match(session['email']):
		flash('Email is not valid.')
		return False

	return True

def validate_password():
	errors = []
	if not PWD_REGEX_UPPER.search(session['password']):
		errors.append('*Password must contain at least 1 upper case character.')
	if not PWD_REGEX_LOWER.search(session['password']):
		errors.append('*Password must contain at least 1 lower case character.')
	if session['password'] != session['confirm_password']:
		errors.append('*Confirm password did not match.')
	
	for err in errors:
		flash(err)

	return (len(errors) == 0)

def add_user():
	pw_hash = bcrypt.generate_password_hash(session['password'])
	sql = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)' 
	sql += ' VALUES (:first, :last, :email, :password, NOW(), NOW()); '
	sql += " SELECT LAST_INSERT_ID() as 'id'"
	query_data = { 'first': session['first'], 'last': session['last'], 'email': session['email'], 'password': pw_hash }
	mysql.query_db(sql, query_data)

app.run(debug=True)
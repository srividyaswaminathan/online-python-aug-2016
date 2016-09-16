#MODULES
from flask import Flask, render_template, redirect, request, session, flash
from connection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

# VARIABLES
app = Flask(__name__) 
app.secret_key = 'ThisIsSecret'
email_regex = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
bcrypt = Bcrypt(app)
db = MySQLConnector(app, 'login_users_db')

# QUERIES
queries = {
	'create': 'INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())',
	'register': 'SELECT * FROM users WHERE first_name=:first_name AND last_name=:last_name AND email=:email AND password=:password',
	'login': 'SELECT * FROM users WHERE email=:email'
}

# ROUTES
@app.route('/')
def index():
	return redirect('/account')

@app.route('/account')
def home():
	# If the user goes back to route, and 'user' is in session, go straight to summary page
	if 'user' not in session: 
		return render_template('login.html')
	else: 
		return redirect('/account/summary')

@app.route('/account/register', methods=['POST'])
def register(): 
	errors = validate('new_user', request.form)
	if errors == []: 
		pw_hash = bcrypt.generate_password_hash(request.form['password'])
		data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
			'password': pw_hash
		}
		db.query_db(queries['create'], data)
		session['user'] = db.query_db(queries['register'], data)
		return redirect('/account/summary')
	else:
		print_flashes(errors)
		return redirect('/account')

@app.route('/account/login/', methods=['POST'])
def login():
	errors = validate('returning_user', request.form)
	if errors == []: 
		data = {
			'email': request.form['email'],
		}
		session['user'] = db.query_db(queries['login'], data)
		return redirect('/account/summary')
	else:
		print_flashes(errors)
		return redirect('/account')

@app.route('/account/summary', methods=['GET'])
def summary():
	return render_template('summary.html')

@app.route('/logout', methods=['GET'])
def logout():
	session.clear()
	return redirect('/account')

# FUNCTIONS
def validate(type, user_input):
	errors = []
	if type == 'new_user': 
		# Required checks for a proper account
		if len(user_input['first_name']) < 2:
			errors.append('First Name must be at least 2 characters.')
		if len(user_input['last_name']) < 2:
			errors.append('Last Name must be at least 2 characters.')
		if not email_regex.match(user_input['email']) or len(user_input['email']) < 8:
			errors.append('Invalid email address. Email must be at least 8 characters long.')
		if len(user_input['password']) < 1:
			errors.append('Password cannot be empty')
		if len(user_input['confirm_password']) < 1:
			errors.append('Please retype your password.')	
		if user_input['password'] != user_input['confirm_password']:
			errors.append('Passwords do not match.')
		data = {
			'email': user_input['email']
		}
		# Prevents duplicate emails from being inserted into the db. 
		duplicate_emails = db.query_db(queries["login"], data)
		if len(duplicate_emails) > 0:
		 	errors.append('User email already exists.')
		return errors

	elif type == 'returning_user':
		password = user_input['password']
		data = {
			'email': user_input['email']	
		}
		user = db.query_db(queries['login'], data)
		if len(user) == 0:
			errors.append('User does not exist.') # Might be better to just say User/Password does not match
		elif not bcrypt.check_password_hash(user[0]['password'], password):	
			errors.append('Wrong Password') # Might be better to just say User/Password does not match
		return errors

def print_flashes(error_list):
	for error in error_list:
		print flash(error, 'error')

if __name__ == '__main__':
	app.run(debug=True)

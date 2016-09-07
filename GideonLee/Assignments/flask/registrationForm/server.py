from flask import Flask, render_template, redirect, request, flash
import re

app = Flask(__name__) 
app.secret_key = 'ThisIsSecret'

email_regex = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
number_regex = re.compile(r'^\d')
password = re.compile(r'^\d.*[A-Z][a-z]|\d.*[a-z][A-Z]|[a-z][A-Z].*\d|[A-Z][a-z].*\d|[A-Z]+\d+[a-z]|[a-z]+\d+[A-Z]')
birthday_regex = re.compile(r'^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$')


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
	# both is to see if both name/last name are invalid and combines them into one flash message
	# both = 0 means both are not invalid. 
	both = 0

	# Checks if both first and last name are invalid. 
	if len(request.form['first_name']) < 1 and len(request.form['last_name']) < 1:
		flash('First name and last name cannot be empty.', 'error')
		both = 1
	if number_regex.match(request.form['first_name']) and number_regex.match(request.form['last_name']):
		flash('First name and last name field cannot contain any numbers', 'error')	
		both = 1
	
	# Checks if first name is valid.
	if len(request.form['first_name']) < 1 and both == 0:
		flash('First name cannot be empty.', 'error')
	elif number_regex.match(request.form['first_name']) and both == 0:
		flash('First name field cannot contain any numbers.', 'error')
	
	# Checks if last name is invalid. 
	if len(request.form['last_name']) < 1 and both == 0:
		flash('Last name cannot be empty.', 'error')
	elif number_regex.match(request.form['last_name']) and both == 0:
		flash('Last name field cannot contain any numbers.', 'error')

	# Checks if date of birth is valid.
	if len(request.form['dob']) < 1:
		flash('Date of Birth cannot be empty.', 'error')
	elif not birthday_regex.match(request.form['dob']):
		flash('Invalid Date/Invalid Format: dd/mm/yyyy', 'error')
	
	# Checks if email is invalid. 
	if len(request.form['email']) < 1:
		flash('Email cannot be empty.', 'error')
	elif not email_regex.match(request.form['email']):
		flash(request.form['email'] + ' is not valid email. (e.g. JonSnow@theWall.watch)', 'error')

	# Checks if password is valid. 
	if len(request.form['password']) < 1:
		flash('Password cannot be empty', 'error')
	elif len(request.form['password']) <= 8: 
		flash('Password must be more than 8 characters.', 'error')
	if not password.match(request.form['password']): 
		flash('Password must have at least 1 uppercase, 1 lowercase, and 1 digit', 'error')

	# Checks if retype_password is valid. 
	if len(request.form['retype_password']) < 1:
		flash('Retype Password cannot be empty', 'error')
	elif request.form['password'] != request.form['retype_password']:
		flash('Passwords do not match.', 'error')
	
	return redirect('/')

app.run(debug=True)

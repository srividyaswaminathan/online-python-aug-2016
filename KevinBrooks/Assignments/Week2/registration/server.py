from flask import Flask, render_template, request, redirect, session, flash
import random, datetime, re
#import logging
#logging.basicConfig(filename='site.log',level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PWD_REGEX_UPPER = re.compile(r'[A-Z]')
PWD_REGEX_LOWER = re.compile(r'[a-z]')

@app.route('/', methods=['get','post'])
def index():
	#logging.info(session)
	if session.has_key('email'):
		return render_template('index.html', email=session['email'], first_name=session['first_name'], last_name=session['last_name'], birth_date=session['birth_date'], sel_type=session['type'])
	else:
		return render_template('index.html', sel_type='ninja')

@app.route('/result', methods=['post'])
def result():
	#logging.info(request.form) 

	session['type'] = request.form['reg_type']
	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['password'] = request.form['password']
	session['confirm_password'] = request.form['confirm_password']

	if request.form.has_key('birth_date'):
		session['birth_date'] = request.form['birth_date']

	if not session.has_key('birth_date'):
		session['birth_date'] = ''
	
	if not validate_all(session):
		return redirect('/')
	else:
		return render_template('result.html', first_name=session['first_name'], last_name=session['last_name'], sel_type=session['type'])

def validate_all(session):
	if not validate_empty(session):
		return False
	if not validate_email(session):
		return False
	if not validate_password(session):
		return False

	if session['type'] == 'hacker':	
		if not validate_date(session):
			return False
		
	return True

def validate_empty(session):
	category = session['type']
	valid = True
	if len(session['email']) < 1:
		flash('*Email cannot be blank.', category)
		valid = False
	if len(session['first_name']) < 1:
		flash('*First Name cannot be blank.', category) 
		valid = False
	if len(session['last_name']) < 1:
		flash('*Last Name cannot be blank.', category)
		valid = False
	if len(session['password']) < 1:
		flash('*Password cannot be blank.', category)
		valid = False
	if len(session['confirm_password']) < 1:
		flash('*Confirm Password cannot be blank.', category)
		valid = False
	if session['type'] == 'hacker':
		if len(session['birth_date']) < 1:
			flash('*Birth Date cannot be blank.', category)
			valid = False

	return valid

def validate_email(session):
	category = session['type']
	if not EMAIL_REGEX.match(session['email']):
		flash('*Invalid email format.', category)
		return False

	return True

def validate_date(session):
	category = session['type']
	try:

		date = datetime.datetime.strptime(session['birth_date'], "%m/%d/%Y")
		
		if datetime.datetime.now() <= date:
			flash('*Birth Date must be in the past.', category)
			return False
	except:
		flash('*Invalid Birth Date.', category)
		return False

	return True

def validate_password(session):
	category = session['type']
	if not PWD_REGEX_UPPER.search(session['password']):
		flash('*Password must contain at least 1 upper case character.', category)
		return False
	if not PWD_REGEX_LOWER.search(session['password']):
		flash('*Password must contain at least 1 lower case character.', category)
		return False

	if session['password'] != session['confirm_password']:
		flash('*Confirm password did not match.', category)
		return False

	return True

app.run(debug=True)
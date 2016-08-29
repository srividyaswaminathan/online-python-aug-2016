from flask import Flask, render_template, request, redirect, session, flash
from flask.ext.bcrypt import Bcrypt
from wallvalidation import *
from walldatabase import *

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 
bcrypt = Bcrypt(app)

@app.route('/', methods=['get'])
def index():
	message_display = 'none'
	if session.has_key('notifications'):
		if len(session['notifications']) > 0:
			message_display = 'block'
			for msg in session['notifications']:
				flash(msg)
	email = ''
	first = ''
	last = ''
	if session.has_key('email'):
		email = session['email']
		first = session['first']
		last = session['last']

	return render_template('index.html', message_display=message_display, first=first, last=last, email=email)

@app.route('/wall', methods=['get'])
def wall():
	if not is_logged_in():
		return redirect('/')
	
	messages = get_messages()

	return render_template('wall.html', first=session['first'], messages=messages)

@app.route('/register', methods=['post'])
def register():
	session['first'] = request.form['first']
	session['last'] = request.form['last']
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	session['confirm_password'] = request.form['confirm_password']
	if not validate_all(session):
		return redirect('/')
	else:
		record = get_user_by_email(session['email'])
		if len(record) > 0:
			session['notifications'].append('Email already exists.')
			return redirect('/')
		else:
			session['login_id'] = add_user(session)
			return redirect('/wall')

@app.route('/login', methods=['post'])
def login():
	session['notifications'] = []
	session['email'] = request.form['email']
	if not validate_email(session):
		session['notifications'] = ['Invalid Email']
		return redirect('/')

	sql = 'SELECT * FROM users WHERE email=:email LIMIT 1'
	query_data = {'email' : request.form['email']}
	
	record = mysql.query_db(sql, query_data)
	session['login_id'] = -1

	if len(record) > 0:
		pw_hash = record[0]['password']
		
		if bcrypt.check_password_hash(pw_hash, request.form['password']):
			session['login_id'] = record[0]['id']
			get_user(session)
			return redirect('/wall')
		else:
			session['notifications'] = ['Invalid Login or Password.']
			return redirect('/')
	else:
		session['notifications'] = ['Invalid Login or Password.']
		return redirect('/')

@app.route('/logoff', methods=['get'])
def logout():
	session.clear()
	return redirect('/')

@app.route('/post_message', methods=['post'])
def post_message():
	if not is_logged_in():
		return redirect('/')

	add_message(request.form['message'], session['login_id'])
		
	return redirect('/wall')

@app.route('/post_comment', methods=['post'])
def post_comment():
	if not is_logged_in():
		return redirect('/')

	msg_id = request.form['msg_id']
	user_id = session['login_id']
	comment = request.form['commentdata']	
	print (comment)
	add_comment(msg_id, user_id, comment)
		
	return redirect('/wall')



def is_logged_in():
	if not session.has_key('login_id'):
		return False

	return (session['login_id'] > 0)
		
app.run(debug=True)
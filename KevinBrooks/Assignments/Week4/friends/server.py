from flask import Flask, render_template, request, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')
# an example of running a query


#print (mysql.query_db("SELECT * FROM emails"))

@app.route('/', methods=['get'])
def index():
	sql = "select id, first_name, last_name, email, date_format(created_at, '%m/%d/%y') as 'created_at' from friends;"
	records = mysql.query_db(sql)
	return render_template('index.html', records=records)

@app.route('/friends', methods=['post'])
def create():
	if request.form.has_key('add'):
		record = [{'id':'', 'first_name' : '', 'last_name' : '', 'email' : ''}]
		return render_template('friends.html', record=record, btn_action='btn_add', crud='Add', message_display='none', friend_id='')	
	elif request.form.has_key('btn_add'):
		session['id'] = request.form['friend_id']
		session['first_name'] = request.form['txt_first']
		session['last_name'] = request.form['txt_last']
		session['email'] = request.form['txt_email']
		if not validate_text() or not validate_email():
			record = [{'id':'', 'first_name' : session['first_name'], 'last_name' : session['last_name'], 'email' : session['email']}]
			return render_template('friends.html', record=record, btn_action='btn_add', crud='Add', message_display='block', friend_id='')
		else:	
			add_friend()
			return redirect('/')

@app.route('/friends/<id>', methods=['post'])
def update(id):
	session['id'] = id
	friend_id = "/" + id
	session['first_name'] = request.form['txt_first']
	session['last_name'] = request.form['txt_last']
	session['email'] = request.form['txt_email']
	if not validate_text() or not validate_email():
		record = [{'id':session['id'], 'first_name' : session['first_name'], 'last_name' : session['last_name'], 'email' : session['email']}]
		return render_template('friends.html', record=record, btn_action='btn_add', crud='Update', message_display='block', friend_id=friend_id)
	else:	
		update_friend_db(id)
		return redirect('/')	

	return render_template('index.html')	

@app.route('/friends/<id>/edit', methods=['post'])
def edit(id):
	record = get_friend(id)
	friend_id = '/' + id
	return render_template('friends.html', record=record, btn_action='btn_edit', crud='Update', message_display='none', friend_id=friend_id)	

@app.route('/friends/<id>/delete', methods=['post'])
def destroy(id):
	delete_friend(id)
	return redirect('/')

def validate_text():
	errors = []
	if len(session['first_name'].strip()) < 1:
		errors.append('First cannot be blank.')
	if len(session['last_name'].strip()) < 1:
		errors.append('Last cannot be blank.')
	if len(session['email'].strip()) < 1:
		errors.append('Email cannot be blank.')
	
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

def add_friend():
	first = "'" + session['first_name'] + "'"
	last = "'" + session['last_name'] + "'"
	email = "'" + session['email'] + "'"
	sql = 'INSERT INTO friends (first_name, last_name, email, created_at, updated_at)' 
	sql += ' VALUES ({0},{1},{2},NOW(), NOW());'.format(first, last, email)
	mysql.query_db(sql)

def update_friend_db(id):
	first = "'" + session['first_name'] + "'"
	last = "'" + session['last_name'] + "'"
	email = "'" + session['email'] + "'"
	sql = 'update friends set first_name = {0}, last_name= {1}, email = {2}, updated_at = NOW() WHERE id = {3};'.format(first, last, email, id)
	mysql.query_db(sql)

def delete_friend(id):
	sql = 'DELETE FROM friends WHERE id = {0};'.format(id)
	mysql.query_db(sql)

def get_friend(id):
	sql = "select id, first_name, last_name, email, date_format(created_at, '%m/%d/%y') as 'created_at' from friends where id={0};".format(id)
	return mysql.query_db(sql)

app.run(debug=True)
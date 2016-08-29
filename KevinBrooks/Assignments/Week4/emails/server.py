from flask import Flask, render_template, request, redirect, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'emails')
# an example of running a query


#print (mysql.query_db("SELECT * FROM emails"))

@app.route('/', methods=['get'])
def index():

	return render_template('index.html', message_display="none")

@app.route('/manage_email', methods=['post'])
def index_post():
	if request.form.has_key('email_check'):
		ids = ''
		for id in request.form.getlist("email_check"):
			ids += id + ","
		else:
			ids = ids[0:len(ids) -1]
		delete_email(ids)
		msg = "Emails Deleted!"
		records = mysql.query_db("SELECT * FROM emails;")
		return render_template('result.html', result_message=msg, records=records)	
	elif request.form.has_key('txt_email'):
		session["email"] = request.form['txt_email']
		if not validate_email():
			return render_template('index.html', message_display="block")	
		else:	
			save_email()
			msg = 'The email address you entered ({0}) is a valid email. Thank You!'.format(session['email'])
			records = mysql.query_db("SELECT * FROM emails;")
	else:
		msg = "Manage Emails"
		records = mysql.query_db("SELECT * FROM emails;")
	return render_template('result.html', result_message=msg, records=records)	

def validate_email():
	if not EMAIL_REGEX.match(session['email']):
		flash('Email is not valid.')
		return False

	return True

def save_email():
	val = "'" + session['email'] + "'"
	sql = 'INSERT INTO emails (email, created_at, updated_at) VALUES ({0},NOW(), NOW());'.format(val)
	mysql.query_db(sql)

def delete_email(ids):
	if len(ids) < 1:
		return

	sql = 'DELETE FROM emails WHERE id in ({0});'.format(ids)
	mysql.query_db(sql)	

app.run(debug=True)
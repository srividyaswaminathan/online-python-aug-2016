from flask import Flask, session, render_template, flash, request, redirect
import re
import os
from datetime import datetime
app = Flask(__name__)
app.secret_key = "SrividyaSwa"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
password_regex = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$')

@app.route('/')
def index():
	#adding form validations
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	email_address = request.form['email_address']  
	first_name = request.form['first_name'] 
	last_name  = request.form['last_name'] 
	password  = request.form['password']
	confirm_password = request.form['confirm_password']
	birthday = request.form['birthday']
	today = datetime.now()
	date_birthday = datetime.strptime(birthday, "%Y-%m-%d")

	print "today is", today
	print "date validation", date_birthday

	if date_birthday > today:
		flash("Birthday cannot be a future date")

	if len(email_address)<1:
		flash("Email cannot be blank")		
	
	if not EMAIL_REGEX.match(email_address):
		flash("Email invalid")
	
	if not first_name.isalpha():
		flash("Name field cannot contain any alpha numeric characters")

	if not last_name.isalpha():
		flash("Name field cannot contain any alpha numeric characters")

	if  password <= 8: 
		flash("Password should be more than 8 characters") 
	
	if password!=confirm_password:
		flash("password and confirm password should match")

	if not password_regex.match(password):
		flash("Password should contain one upper case letter and a number")

	return render_template('results.html')


app.run(debug=True,host=os.getenv('IP', '0.0.0.0'))	

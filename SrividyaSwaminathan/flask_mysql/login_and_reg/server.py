from flask import Flask, session, render_template, request, redirect, flash
import re
from flask_bcrypt import Bcrypt 
from mysqlconnection import MySQLConnector
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, "login_and_registration")
app.secret_key = "ThisisaSecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
queries = {
			"insert_user" : "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW())",
			"get_user": "SELECT * FROM users WHERE email= :email LIMIT 1"
}
def get_user(email_address):
	query = queries["get_user"]
	data = {
			"email": email_address	
	}
	user = mysql.query_db(query, data)
	return user	

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success', methods=['POST'])
def create_user():
	print "received create user request"
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email_address = request.form['email']
	password = request.form['password']
	confirm_password = request.form['password_confirm']
	valid_fields = True
	if len(first_name)<2 and len(last_name)<2:
		flash("Please enter your full name")
		valid_fields = False
	if not EMAIL_REGEX.match(email_address):
		flash("Please enter a valid email address")
		valid_fields = False
	if len(password) <8:
		flash("Enter a password of minimum 8 characters")
		valid_fields = False
	if password != confirm_password:
		flash("Passwords do not match")
		valid_fields = False
	email_address = request.form['email']
	user = get_user(email_address)
	if len(user) > 0:
		flash("email address is already registered")
		valid_fields = False

	print "validated request fields, valid=", valid_fields
	if valid_fields:
		pw_hash = bcrypt.generate_password_hash(password)	
		query = queries['insert_user']
		data = {
				"first_name": first_name,
				"last_name": last_name,
				"email": email_address,
				"pw_hash": pw_hash
		}	
		user = mysql.query_db(query, data)
		return render_template('success.html', operation="Registration")
	else:
		return redirect('/')	

@app.route('/login', methods=['POST'])
def login():

	password = request.form['password']
	email_address = request.form['email']
	user = get_user(email_address)
	if bcrypt.check_password_hash(user[0]['pw_hash'], password):
		session["logged_in_user"] = email_address
		return render_template('success.html', operation="Login") 
	else:
		flash("Please enter correct login credentials")
		return redirect('/')

		
app.run(debug=True)
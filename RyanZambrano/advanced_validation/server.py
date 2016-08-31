from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
	if len(request.form['first_name']) < 1:
		flash("Please enter your first name")
	if len(request.form['last_name']) < 1:
		flash("Please enter your last name")
	if len(request.form['password']) < 9:
		flash("Password must be more than 8 characters.")
	if request.form['confirm_password'] != request.form['password']:
		flash("Passwords do not match.")
		
	else:
		flash("Success!")
	return redirect('/')
app.run(debug=True)
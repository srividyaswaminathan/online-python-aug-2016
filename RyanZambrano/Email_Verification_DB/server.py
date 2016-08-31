from flask import Flask, render_template, request, redirect, flash
from connection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation')
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')
app.secret_key = 'secret'

# mysql queries
queries = {
	'create' : "INSERT INTO emails (email, created_at) VALUES (:email, NOW());",
	'index' : "SELECT * FROM emails",
	'delete' : "DELETE FROM emails WHERE id = :id"
}

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		print "FORM SUBMITTED"
		if(validateEmail(request.form['email'])):
			query = queries['create']
			data = { 'email' : request.form['email'] }
			mysql.query_db(query, data)
			flash('Successfully created email record')
			return redirect('/success')
		else:
			flash('Not a valid email')
	return render_template('index.html')

@app.route('/success', methods=["GET"])
def success():
	query = queries['index']
	data = {}
	emails = mysql.query_db(query, data)
	print emails
	return render_template('success.html', emails=emails)

@app.route('/<id>', methods=["POST"])
def destroy(id):
	query = queries['delete']
	data = {
		'id' : id
	}
	flash('Successfully deleted email')
	emails = mysql.query_db(query, data)
	return redirect('/success')

def validateEmail(email):
	return EMAIL_REGEX.match(email)

app.run(debug=True)
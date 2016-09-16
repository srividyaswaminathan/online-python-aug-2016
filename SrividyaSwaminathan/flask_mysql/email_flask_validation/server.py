from flask import Flask, request, redirect, session, flash, render_template
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, "email_db")
app.secret_key = "ThisIsSecret!"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

queries = {
	"create": "INSERT INTO users (email, created_at) VALUES (:email_address, NOW())",
	"show" : "SELECT * from users",
	"delete": "DELETE FROM users WHERE id= :specific_id"
}


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit_email():
	email = request.form['email_address']
	if not EMAIL_REGEX.match(email):
		flash("Invalid email address")
		return redirect("/")
	else:
		# insert the row
		query = queries['create']
		data = {
			'email_address' : email
		}
		users = mysql.query_db(query, data)	
		flash("Thank you for entering a valid email address")
		return redirect("/users")

# /remove/<id>
@app.route('/remove/<id>')
def remove_email(id):
	query = queries['delete']
	data = {
		'specific_id': id
	}
	mysql.query_db(query, data)	
	flash("Thank you for deleting email address")
	return redirect("/users")

@app.route('/users')
def show_emails():
	query = queries['show']
	data = {}
	users = mysql.query_db(query, data)
	return render_template("success.html", all_users=users)	

app.run(debug=True)	
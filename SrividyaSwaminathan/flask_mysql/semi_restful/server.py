from flask import Flask, session, render_template, request, redirect, flash
import re
from flask_bcrypt import Bcrypt 
from mysqlconnection import MySQLConnector
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, "semi_restful_users")
app.secret_key = "ThisisaSecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile('^[A-Za-z\s]*$')
#dictionary to hold all queries 
queries = {
			"show_users": "SELECT * FROM users",
			"create_user": "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())",
			"show_one_user": "SELECT * FROM users WHERE id= :id",	
			"update_user": "UPDATE users SET first_name= :first_name, last_name= :last_name, email= :email, created_at= NOW(), updated_at= NOW()) WHERE id= :id",
			"delete_user": "DELETE FROM users WHERE id= :id"
			}

@app.route("/users")
def index():
	query = queries['show_users']
	users = mysql.query_db(query)
	print users
	return render_template("index.html", users=users )

@app.route("/users/new")
def new():
	return render_template("new_user.html")

@app.route("/users/<id>/edit")
def edit(id):
	return render_template("edit.html", id=id)

@app.route("/users/<id>")
def display(id):
	query = queries['show_one_user']
	data = {
			'id': id
	}
	user = mysql.query_db(query, data)
	return render_template("show.html", user=user[0], id=id)

@app.route("/users/create", methods=["POST"])
def create():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	#validations 
	valid_fields = True 
	if len(first_name)<2 :
		flash("Enter a valid name")
		valid_fields = False
	if len(last_name)<2:
		flash("Enter a valid name")
		valid_fields = False	 
	if not EMAIL_REGEX.match(email):
		flash("Enter a valid email")
		valid_fields = False

	if valid_fields:
		query = queries['create_user']
		data = {
					'first_name': first_name,
					'last_name': last_name,
					'email': email,

			}
		user = mysql.query_db(query, data)
		return redirect('/users')

	else:
		return redirect("/users/new")	

#GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
@app.route("/users/<id>/destroy")
def destroy(id):
	print "destroy", id
	query = queries['delete_user']
	print "destroy query ", query
	data = {
			 'id': id
	}
	print "destroy", data
	user = mysql.query_db(query, data)	
	return redirect('/users')
	

#POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated. ASK  	
@app.route("/users/<id>", methods=["POST"])
def update():
	query = queries['update_user']
	data = {
				'id': id
		}	
	user = mysql.query_db(query, data)	
	return redirect("/users/<id>")

app.run(debug=True)				
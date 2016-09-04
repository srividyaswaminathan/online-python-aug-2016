"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
03-September-2015
Python > Flask & MySQL > Optional Assignment: Semi-Restful Users
"""

from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.secret_key = "TheAnswerToLifeTheUniverseAndEverything=42"
db = MySQLConnector(app,'user_db')
EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

queries = {
    'index'  : "SELECT * FROM users",
    'create' : "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())",
    'select_id' : "SELECT * FROM users WHERE id=:id",
    'update' : "UPDATE users SET first_name = :first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id=:id",
    'delete' : "DELETE FROM users WHERE id=:id"
}

print db.query_db("SELECT * FROM users")

# ROUTING
@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def user():
    """
    GET request to /users - calls the index method to display all the users. This will need a template.
    """
    query = queries['index']
    data = {}
    all_users = db.query_db(query, data)

    return render_template('index.html', all_users=all_users)

@app.route('/users/new')
def new():
    """
    GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.
    """
    return render_template('new.html')

@app.route('/users/<id>/edit')
def edit(id):
    """
    GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
    """
    query = queries['select_id']
    data = {
        'id' : id
    }
    user = db.query_db(query, data)[0]

    return render_template('edit.html', user=user)

@app.route('/users/<id>', methods=["GET"])
def show(id):
    """
    GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.
    """
    query = queries['select_id']
    data = {
        'id' : id
    }
    user = db.query_db(query, data)[0]

    return render_template('show.html', user=user)

@app.route('/users/create',  methods=["POST"])
def create():
    """
    POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
    """
    query = queries['create']
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    user_id = db.query_db(query, data)

    return redirect('/users/'+str(user_id))

@app.route('/users/<id>/destroy')
def destroy(id):
    """
    GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
    """
    query = queries['delete']
    data = {
        'id' : id
    }

    db.query_db(query, data)

    return redirect('/users')

@app.route('/users/<id>',  methods=["POST"])
def update(id):
    """
    POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.
    """
    query = queries['update']
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' : id
    }

    db.query_db(query, data)

    return redirect('/users/'+str(id))

app.run(debug=True)

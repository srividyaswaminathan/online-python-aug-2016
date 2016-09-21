"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
02-September-2015
Python > Flask & MySQL > Assignment: The Wall
"""

from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "TheAnswerToLifeTheUniverseAndEverything=42"
db = MySQLConnector(app,'wall_db')

EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

queries = {
    'user' :
    {
        'create' : "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())",
        'index'  : "SELECT * FROM users",
        'delete' : "DELETE FROM users WHERE id=:id",
        'select_id' : "SELECT * FROM users WHERE id=:id",
        'update' : "UPDATE users SET first_name = :first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id=:id",
        'select_email' : "SELECT id, password FROM users WHERE email=:email"
    },
    'message' :
    {
        'create' : "INSERT INTO messages (message, user_id, created_at, updated_at) VALUES (:message, :user_id, NOW(), NOW())",
        'index'  : "SELECT * FROM messages"

    },
    'comment' :
    {
        'create' : "INSERT INTO comments (comment, message_id, user_id, created_at, updated_at) VALUES (:comment, :message_id, :user_id, NOW(), NOW())",
        'index'  : "SELECT * FROM comments"
    }


}

# ROUTING
@app.route('/')                                     # '/' (GET) login/registration form
def index():
    if 'user' in session:
        return redirect('/wall')

    return render_template('index.html')


@app.route('/logout')                               # '/logout' (GET) pop user from session and redirect to root
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/login', methods=["POST"])              # '/login' (POST) login a registered user
def login():
    query = queries['user']['select_email']

    data = {
        'email' : request.form['email']
    }

    pot_user = db.query_db(query, data)

    if len(pot_user) < 1:
        flash('No such user found', 'error')
        return redirect('/')

    if bcrypt.check_password_hash(pot_user[0]['password'], request.form['password']):
        return login_user(pot_user[0]['id'])
    else:
        flash('Invalid login', 'error')
        return redirect('/')


    return redirect('/')

@app.route('/register', methods=["POST"])           # '/register' (POST) register a new user / login new user
def create():

    if not (is_name_valid(request.form['first_name']) and is_name_valid(request.form['last_name'])):
        flash('Name is not valid!', 'error')
        return redirect('/')
    if not is_email_valid(request.form['email']):
        flash('Email is not valid!', 'error')
        return redirect('/')
    if not is_password_valid(request.form['password']):
        flash('Password should be at least 8 characters', 'error')
        return redirect('/')
    if not do_passwords_match(request.form['password'], request.form['password_confirmation']):
        flash('Password confirmation does not match', 'error')
        return redirect('/')

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : encrypt_password(request.form['password'])
    }
    query = queries['user']['create']
    new_user_id = db.query_db(query, data)

    return login_user(new_user_id)


@app.route('/wall', methods=["GET"])             # '/wall' (GET) go to the wall
def wall():

    if not 'user' in session:
        flash('Please Login', 'error')
        return redirect('/')

    query = queries['message']['index']
    messages = db.query_db(query)

    query = queries['comment']['index']
    comments = db.query_db(query)

    query = queries['user']['index']
    users = db.query_db(query)


    return render_template('wall.html', messages=messages, comments=comments, users=users)

@app.route('/message', methods=["POST"])             # '/message' (POST) add/display message to wall
def message():
    print request.form['message']

    query = queries['message']['create']
    print query
    data = {
        'message' : request.form['message'],
        'user_id' : session['user']['id']
    }

    message_id = db.query_db(query, data)
    print message_id
    return redirect('/wall')

@app.route('/comment', methods=["POST"])             # '/comment' (POST) add/display comment to wall
def comment():
    message_id = request.form['message_id']
    print message_id
    query = queries['comment']['create']
    print query
    data = {
        'comment'    : request.form['comment'],
        'message_id' : message_id,
        'user_id'    : session['user']['id']
    }

    comment_id = db.query_db(query, data)

    return redirect('/wall')

# Helper Functions
def is_email_valid(email):
    return EMAIL_REGEX.match(email)

def is_name_valid(name):
    return len(name) > 1 and name.isalpha()

def is_password_valid(pwd):
    return len(pwd) > 7

def encrypt_password(pwd):
    return bcrypt.generate_password_hash(pwd)

def decrypt_password(pwd):
    return pwd #Not Implemented

def do_passwords_match(pwd, pwd_con):
    return pwd == pwd_con

def login_user(id):
    query = queries['user']['select_id']
    data = {
        'id' : id
    }
    user = db.query_db(query, data)[0]
    session['user'] = user

    return redirect('/wall')

app.run(debug=True)

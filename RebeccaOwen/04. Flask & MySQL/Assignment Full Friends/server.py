"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
30-August-2015
Python > Flask & MySQL > Assignment: Full Friends
"""

from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "somesecret"
db = MySQLConnector(app,'friends_db')

EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

queries = {
    'create' : "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())",
    'index'  : "SELECT * FROM friends",
    'delete' : "DELETE FROM friends WHERE id=:id",
    'select' : "SELECT * FROM friends WHERE id=:id",
    'update' : "UPDATE friends SET first_name = :first_name, last_name=:last_name, email=:email WHERE id=:id"
}

print db.query_db("SELECT * FROM friends")

# ROUTING
@app.route('/')                                         #Show All Friends
def index():
    query = queries['index']
    data = {}
    all_friends = db.query_db(query, data)

    return render_template('index.html', all_friends = all_friends)

@app.route('/friends', methods=["POST"])                #Create A Friend
def create():
    if is_email_valid(request.form['email']):
        query = queries['create']
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email']
        }
        db.query_db(query, data)
        msg = request.form['first_name'] + ' is your new friend!'
        flash(msg, 'success')
    else:
        flash('Email is not valid!', 'error')

    return redirect('/')

@app.route('/friends/<id>', methods=["POST"])           #Update A Friend
def update(id):
    if is_email_valid(request.form['email']):
        query = queries['update']
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'id' : id
        }
        db.query_db(query, data)
        msg = request.form['first_name'] + ' has been updated!'
        flash(msg, 'success')
    else:
        flash('Email is not valid!', 'error')

    return redirect('/')

@app.route('/friends/<id>/edit', methods=["GET"])       #Show Form to edit A Friend
def edit(id):
    query = queries['select']
    data = {
        'id' : id
    }
    friend = db.query_db(query, data)

    return render_template('edit.html', friend=friend[0])


@app.route('/friends/<id>/delete', methods=["POST"])    #Delete A Friend
def delete(id):
    query = queries['select']
    data = {
        'id' : id
    }
    friend = db.query_db(query, data)

    query = queries['delete']
    db.query_db(query, data)

    msg = 'So long ' + friend[0]['first_name'] + ' it was nice knowing you!'
    flash(msg, 'success')

    return redirect('/')


def is_email_valid(email):
    return EMAIL_REGEX.match(email)

app.run(debug=True)

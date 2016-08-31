"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
24-August-2015
Python > Flask & MySQL > Assignment: Email Validation with DB
"""

from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "somesecret"
db = MySQLConnector(app,'emaildb')

EMAIL_REGEX = re.compile(r'^[\w\.+_-]+@[\w\._-]+\.[\w]*$')

queries = {
    'create' : "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW());",
    'index' : "SELECT * FROM emails",
    'delete' : "DELETE FROM emails WHERE id=:id;"
}


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if is_email_valid(request.form['email']):
            query = queries['create']
            data = {
                'email' : request.form['email']
            }
            db.query_db(query, data)
            msg = 'The email address you entered (' + request.form['email'] + ') is a VALID email address! Thank you!'
            flash(msg, 'success')
            return  redirect('/success')
        else:
            flash('Email is not valid!', 'error')
    return render_template('index.html') # pass data to our template

@app.route('/success', methods=["GET"])
def success():
    query = queries['index']
    all_emails = db.query_db(query)
    return render_template('success.html', all_emails=all_emails)

@app.route('/delete/<id>', methods=["POST"])
def delete(id):
    query = queries['delete']
    data = {
        'id' : id
    }
    msg = 'Deleted Email Record: ' +str(id)
    flash(msg, 'success')
    db.query_db(query, data)

    return redirect('/success')



def is_email_valid(email):
    return EMAIL_REGEX.match(email)

app.run(debug=True)

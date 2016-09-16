from flask import Flask, request, render_template, redirect, session, flash, url_for
from connection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'Its A Secret'
mysql = MySQLConnector(app, 'friendsdb')
name_regex = re.compile('^[A-Za-z\s]*$')
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    query = "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%Y %b %d, %l:%i %p') AS updated FROM friends"
    friends = mysql.query_db(query)
    # print friends
    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    user = request.form
    invalid = False
    if len(''.join(user['first_name'].split(' '))) < 1:
        invalid = True
        flash("Please enter your first name!","first_error")
    elif not name_regex.match(user['first_name']):
        invalid = True
        flash("First name is not valid!","first_error")

    if len(''.join(user['last_name'].split(' '))) < 1:
        invalid = True
        flash("Please enter your last name!","last_error")
    elif not name_regex.match(user['last_name']):
        invalid = True
        flash("Last name is not valid!","last_error")

    if len(user['email']) < 1:
        invalid = True
        flash("Please enter your email!","email_error")
    elif not email_regex.match(user['email']):
        invalid = True
        flash("Email is not valid!","email_error")
    if invalid:
        return redirect('/')
    query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first, :last, :email, NOW())"
    data = {
            'first': ''.join(request.form['first_name'].split(' ')).capitalize(),
            'last': ''.join(request.form['last_name'].split(' ')).capitalize(),
            'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends WHERE id =:id"
    data = {'id': id}
    friends = mysql.query_db(query, data)
    return render_template('edit.html', friends=friends)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    user = request.form
    url = "/friends/"+id+"/edit"
    if not name_regex.match(user['first_name']):
        flash("First name is not valid!","first_update_error")
    elif (''.join(user['first_name'].split(' '))) != "":
        query = "UPDATE friends SET first_name = :first WHERE id =:id"
        data = {'first': ''.join(user['first_name'].split(' ')).capitalize(), 'id': id}
        mysql.query_db(query, data)

    if not name_regex.match(user['last_name']):
        flash("Last name is not valid!","last_update_error")
    elif ''.join(user['last_name'].split(' ')) != "":
        query = "UPDATE friends SET last_name = :last WHERE id =:id"
        data = {'last': ''.join(user['last_name'].split(' ')).capitalize(), 'id': id}
        mysql.query_db(query, data)

    if ''.join(user['email'].split(' ')) != "" and email_regex.match(user['email']):
        query = "UPDATE friends SET email = :email WHERE id =:id"
        data = {'email': user['email'], 'id': id}
        mysql.query_db(query, data)
    elif ''.join(user['email'].split(' ')) != "" and not email_regex.match(user['email']):
        flash("Email is not valid!","email_update_error")
    return redirect(url)

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

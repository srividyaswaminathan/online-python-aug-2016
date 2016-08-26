from flask import Flask, render_template, redirect, request, session, flash, url_for
from connection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'Its A Secret'
mysql = MySQLConnector(app, 'usersdb')
name_regex = re.compile('^[A-Za-z\s]*$')
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
pw_regex = re.compile(r'\s+')

@app.route('/')
def index():
    try:
        session['id']
    except:
        return render_template('index.html')
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {'email': request.form['email']}
    account = mysql.query_db(query, data)
    if account:
        if bcrypt.check_password_hash(account[0]['pw_hash'], request.form['password']):
            session['id'] = account[0]['id']
            return redirect('/success')
        else:
            flash("Incorrect password!","login_pw_error")
    else:
        flash("Email address doesn't exist!","login_account_error")
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    invalid = False
    user = request.form
    first = ''.join(user['first_name'].split(' ')).capitalize()
    last = ''.join(user['last_name'].split(' ')).capitalize()
    pw = ''.join(user['pw'].split(' '))
    if len(first) < 1:
        invalid = True
        flash("Please enter your first name!","first_error")
    elif len(first) < 2 or not name_regex.match(first):
        invalid = True
        flash("First name is not valid!","first_error")

    if len(last) < 1:
        invalid = True
        flash("Please enter your last name!","last_error")
    elif len(last) < 2 or not name_regex.match(last):
        invalid = True
        flash("Last name is not valid!","last_error")

    if len(user['email']) < 1:
        invalid = True
        flash("Please enter your email!","email_error")
    elif not email_regex.match(user['email']):
        invalid = True
        flash("Email is not valid!","email_error")

    if len(pw) < 1:
        invalid = True
        flash("Please create a new password.","pw_error")
    elif pw_regex.match(user['pw']) or len(pw) < 8:
        invalid = True
        flash("Please create a new password as per the criteria.","pw_error")

    if not user['confirm_pw'] == user['pw']:
        invalid = True
        flash("The passwords entered don't match.","confirm_error")

    if invalid:
        return redirect('/')
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {'email': user['email']}
    account = mysql.query_db(query, data)
    if account:
        flash("Email address already exists!","reg_error")
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(user['pw'])
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first, :last, :email, :password, NOW(), NOW())"
        data = {
                'first': first,
                'last': last,
                'email': user['email'],
                'password': pw_hash
        }
        mysql.query_db(query, data)
        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': user['email']}
        account = mysql.query_db(query, data)
        session['id'] = account[0]['id']
    return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM users WHERE id = :id"
    data = {'id': session['id']}
    user = mysql.query_db(query, data)
    return render_template('success.html', user=user)

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'Its A Secret'
mysql = MySQLConnector(app, 'emailsdb')
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    try:
        session['email']
    except:
        session['email'] = ""
    return render_template('index.html')

@app.route('/process', methods=['POST','GET'])
def process():
    session['email'] = request.form['email']
    if not email_regex.match(session['email']):
        flash("Email is not valid!")
        return redirect('/')
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    data = {'email': request.form['email']}
    emails = mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def show():
    query = "SELECT id, email, DATE_FORMAT(created_at,'%b %D, %Y, %l:%i %p') AS created_at FROM emails"
    emails = mysql.query_db(query)
    print emails
    return render_template('success.html', emails=emails)

@app.route('/remove/<email_id>')
def remove(email_id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    return redirect('/success')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, redirect, request, session, flash, url_for
from connection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'Its A Secret'
mysql = MySQLConnector(app, 'walldb')
name_regex = re.compile('^[A-Za-z\s]*$')
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
pw_regex = re.compile('\s+')

@app.route('/')
def index():
    try:
        session['id']
        query = "SELECT * FROM users WHERE id = :id"
        data = {'id': session['id']}
        user = mysql.query_db(query, data)
        user[0]
    except:
        return render_template('index.html')

    return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
    query = "SELECT * FROM users WHERE email = :email"
    data = {'email': request.form['email']}
    account = mysql.query_db(query, data)
    if account:
        if bcrypt.check_password_hash(account[0]['pw_hash'], request.form['password']):
            session['id'] = account[0]['id']
            return redirect('/wall')
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
    query = "SELECT * FROM users WHERE email = :email"
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
    return redirect('/wall')

@app.route('/wall')
def wall():
    query = "SELECT users.id AS user_id, messages.id AS msg_id, first_name, last_name, message, TIMESTAMPDIFF(MINUTE, messages.created_at, NOW()) AS time_offset, DATE_FORMAT(messages.created_at, '%M %D %Y, %l:%i %p') AS msg_created FROM users JOIN messages ON messages.user_id = users.id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(query)
    query = "SELECT messages.id AS msg_id, first_name, last_name, comment, DATE_FORMAT(comments.created_at, '%M %D %Y, %l:%i %p') AS comment_created FROM users JOIN comments ON users.id = comments.user_id JOIN messages ON messages.id = comments.message_id ORDER BY comments.created_at"
    comments = mysql.query_db(query)
    query = "SELECT * FROM users WHERE id = :id"
    data = {'id': session['id']}
    user = mysql.query_db(query, data)
    return render_template('wall.html', user=user, messages=messages, comments=comments)

@app.route('/message',methods=['POST'])
def post_message():
    message = request.form['message']
    if len(''.join(message.split(' '))) < 1:
        flash("Please enter your message!")
        return redirect('/wall')
    query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:id, :message, NOW(), NOW())"
    data = {'id': session['id'], 'message': message}
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/message/<id>/delete', methods=['POST'])
def message_delete(id):
    query = "SELECT * FROM messages WHERE TIMESTAMPDIFF(MINUTE, messages.created_at, NOW()) <= 30 and id =:id"
    data = {'id': id}
    msg_del = mysql.query_db(query, data)
    if not msg_del:
        flash("You're not allowed to delete your message that was made more than 30 minutes!")
        return redirect('/wall')
    flash("Message deleted!")
    query = "DELETE FROM messages WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comment/<id>', methods=['POST'])
def post_comment(id):
    comment = request.form['comment']
    if len(''.join(comment.split(' '))) < 1:
        flash("Please enter your comment!")
        return redirect('/wall')
    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:id, :msg_id, :comment, NOW(), NOW())"
    data = {
            'id': session['id'],
            'msg_id': id,
            'comment': comment
    }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/logout')
def logout():
    session.pop('id')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

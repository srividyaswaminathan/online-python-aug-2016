from flask import Flask, render_template, request, redirect, flash, session
import re
app = Flask(__name__)
app.secret_key = 'Its A Secret'

name_regex = re.compile('^[A-Za-z\s]+$')
email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$')
pw_regex = re.compile(r'.*?[A-Z]+.*?[0-9]+|.*?[0-9]+.*?[A-Z]')

@app.route('/')
def index():
    if 'first' not in session:
        session['first'] = ''
    if 'last' not in session:
        session['last'] = ''
    if 'email' not in session:
        session['email'] = ''
    if 'pw' not in session:
        session['pw'] = ''
    if 'confirm_pw' not in session:
        session['confirm_pw'] = ''
    return render_template("index.html")

@app.route('/register', methods=['POST','GET'])
def register():
    user = request.form
    invalid = False
    style = 'border:1px solid orangered'

    if len(''.join(user['first_name'].split(' '))) < 1:
        invalid = True
        session['first'] = style
        flash("Please enter your first name.","firstname_error")
    elif not name_regex.match(user['first_name']) and user['first_name'] != '':
        invalid = True
        session['first'] = style
        flash("Include invalid characters.","firstname_error")
    else:
        session['first'] = ''

    if len(''.join(user['last_name'].split(' '))) < 1:
        invalid = True
        session['last'] = style
        flash("Please enter your last name.","lastname_error")
    elif not name_regex.match(user['last_name']):
        invalid = True
        session['last'] = style
        flash("Include invalid characters.","lastname_error")
    else:
        session['last'] = ''

    if len(''.join(user['email'].split(' '))) < 1:
        invalid = True
        session['email'] = style
        flash("Please enter your email address.","email_error")
    elif not email_regex.match(user['email']):
        invalid = True
        session['email'] = style
        flash("You have entered an invalid email address.","email_error")
    else:
        session['email'] = ''

    if len(''.join(user['password'].split(' '))) < 1:
        invalid = True
        session['pw'] = style
        flash("Please create a new password.","pw_error")
    elif (not pw_regex.match(user['password'])) or len(user['password']) < 8:
        invalid = True
        session['pw'] = style
        flash("Please create a new password as per the password criteria.","pw_error")
    else:
        session['pw'] = ''

    if not user['password'] == user['confirm_password']:
        invalid = True
        session['confirm_pw'] = style
        flash("The passwords entered don't match.","confirm_pw_error")
    else:
        session['confirm_pw'] = ''

    if invalid:
        return redirect('/')
    name = ''.join(user['first_name'].split(' ')).capitalize()
    msg = 'Hi,'+name+'! Thanks for submitting your information!'
    return render_template("index.html",msg=msg)

if __name__ == '__main__':
    app.run(debug=True)

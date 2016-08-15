"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
14-August-2015
Python > Flask > Assignment: Assignment: Registration Form
"""

from flask import Flask, render_template, request, redirect, session, flash
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    form = {}

    form['email'] = request.form['email']
    form['first_name'] = request.form['first_name']
    form['last_name'] = request.form['last_name']
    form['password'] = request.form['password']
    form['confirm_password'] = request.form['confirm_password']

    print form

    if len(form['email']) < 1:
        flash("Email cannot be blank!", 'error')
    elif not EMAIL_REGEX.match(form['email']):
        flash("Invalid Email Address!", 'error')
    elif len(form['first_name']) < 1 or len(form['last_name']) < 1:
        flash("Name cannot be blank!", 'error')
    elif not (form['first_name'].isalpha() and form['last_name'].isalpha()):
        flash("Name cannot contain any numbers!", 'error')
    elif len(form['password']) < 9:
        flash("Password should contain more than 8 characters!", 'error')
    elif form['password'] != form['confirm_password']:
        flash("Password confirmation does not match!", 'error')
    else:
        flash("Thanks for submitting your information.", 'success')

    return redirect('/')

app.run(debug=True)                       # Run the app in debug mode.
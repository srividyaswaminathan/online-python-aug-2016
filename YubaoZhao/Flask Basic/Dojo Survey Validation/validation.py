from flask import Flask, render_template, request, redirect, flash, session
import re
app = Flask(__name__)
app.secret_key = 'Its A Secret'

@app.route('/')
def index():
    if 'name' not in session:
        session['name'] = ''
    if 'comment' not in session:
        session['comment'] = ''
    return render_template("index.html")

@app.route('/process', methods=['POST','GET'])
def result():
    name_regex = re.compile('^[A-Za-z\s]+$')
    user_data = request.form
    invalid = False
    name = False
    comment = False
    style = 'border:2px solid red'
    if len(''.join(user_data['username'].split(' '))) < 1:
        invalid = True
        name = True
        flash("Name field cannot be blank!","name_error")
    if not name_regex.match(user_data['username']) and user_data['username'] != '':
        invalid = True
        name = True
        flash("Invalid input! Contains non-letter character.","name_error")
    if len(''.join(user_data['comment'].split(' '))) > 120:
        invalid = True
        comment = True
        flash("No more than 120 characters!","comment_error")
    if len(''.join(user_data['comment'].split(' '))) < 1:
        invalid = True
        comment = True
        flash("Comment field cannot be blank!","comment_error")
    if name:
        session['name'] = style
    else:
        session['name'] = ''
    if comment:
        session['comment'] = style
    else:
        session['comment'] = ''
    if invalid:
        return redirect('/')

    session.pop('name')
    session.pop('comment')
    # print user_dat
    return render_template("process.html",data=user_data)

if __name__ == '__main__':
    app.run(debug=True)

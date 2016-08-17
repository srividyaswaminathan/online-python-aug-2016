"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
13-August-2015
Python > Flask > Assignment: Dojo Survey With Validation
"""

from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    print "Got Post Info"
    nam = request.form['name']
    loc = request.form['location']
    lan = request.form['language']
    com = request.form['comment']
    if len(nam) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    elif len(com) > 120:
        flash("Comments must be less than 120 characters!")
        return redirect('/')
    elif len(com) < 1:
        flash("Comments are not really optional!!!")
        return redirect('/')

    return render_template("result.html", nam=nam, loc=loc, lan=lan, com=com)

app.run(debug=True)                       # Run the app in debug mode.
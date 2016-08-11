"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
10-August-2015
Python > Flask > Assignment: Dojo Survey
"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

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
    print nam, loc, lan, com

    return render_template("result.html", nam=nam, loc=loc, lan=lan, com=com)

app.run(debug=True)                       # Run the app in debug mode.
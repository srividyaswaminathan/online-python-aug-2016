"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
11-August-2015
Python > Flask > Assignment Great Number Game
"""

import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'



@app.route('/')
def index():
    if 'randomNumber' not in session:
        session['randomNumber'] = random.randrange(0, 101) # random number between 1-100
        print session['randomNumber']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def result():
    guess = request.form['guess']

    print guess, session['randomNumber']

    if guess == session['randomNumber']:
        print 'YOU GOT IT!!!'
    elif guess < session['randomNumber']:
        print 'Too Low'
    elif guess > session['randomNumber']:
        print 'Too High'


    return redirect('/')


app.run(debug=True)                       # Run the app in debug mode.
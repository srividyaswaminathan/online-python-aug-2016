"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
11-August-2015
Python > Flask > Assignment Great Number Game
"""

from random import randrange # import the random module
# The random module has many useful functions. This is one that gives a random number in a range

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'answer' not in session:
        session['answer'] = randrange(1, 101) # random number between 1-100
        session['result'] = "NA"
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def result():
    guess = int(request.form['guess'])

    if guess == session['answer']:
        session['result'] = " was the number!"
    elif guess < session['answer']:
        session['result'] = "Too Low!"
    else:
        session['result'] = "Too High!"


    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('answer')
    return redirect('/')

app.run(debug=True)                       # Run the app in debug mode.
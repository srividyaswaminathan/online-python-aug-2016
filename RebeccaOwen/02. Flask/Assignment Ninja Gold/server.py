"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
13-August-2015
Python > Flask > Assignment Ninja Gold
"""

from random import randrange # import the random module
# The random module has many useful functions. This is one that gives a random number in a range
from datetime import datetime

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'score' not in session:
        session['score'] = 0
        session['msg'] = []
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    p = {}
    gold = 0
    building = request.form['building']
    time = ' ('+datetime.now().strftime("%x %I:%M%p")+')'

    if building == 'casino':
        gold = randrange(-50, 51)
    elif building == 'house':
        gold = randrange(2, 6)
    elif building == 'cave':
        gold = randrange(5, 11)
    elif building == 'farm':
        gold = randrange(10, 21)

    if gold < 0:
        p['color'] = 'red'
        p['message'] = 'Entered a '+building+ ' and lost ' +str(gold*-1)+ ' golds... Ouch... ' +time
    else:
        p['color'] = 'green'
        p['message'] = 'Earned ' +str(gold)+ ' golds from the '+building+ '! ' +time

    session['score'] += gold
    session['msg'] = [p] + session['msg']

    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('score')
    session.pop('msg')
    return redirect('/')

app.run(debug=True)                       # Run the app in debug mode.
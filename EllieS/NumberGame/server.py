from flask import Flask, session,render_template, request, redirect
import random
from random import randrange

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def numberGame ():
    if 'answer' not in session:
        session['answer']= random.randint(1, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if session['answer'] == guess:
        session['result'] = "you got it!"
    elif session['answer'] < guess:
        session['result'] = "too low!"
    else:
        session['result'] = "too high!"
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('answer')
    return redirect('/')
app.run(debug=True)

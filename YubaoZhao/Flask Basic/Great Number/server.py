from flask import Flask, request, render_template, redirect, session
from random import randint
app = Flask(__name__)
app.secret_key = 'Its A Secret'

@app.route('/', methods = ['GET','POST'])
def index():
    try:
        session['random']
        session['counter']
    except:
        session['random'] = randint(1,100)
        session['counter'] = 0
    print "Random number: %d"%session['random']
    print "Counter: %d"%session['counter']
    data = {}
    guess = 0
    try:
        num = int(request.form['number'])
        guess = request.form['number']
        print "Your input: %d"%num
        session['counter'] += 1
        if num == session['random']:
            data['correct'] = "true"
            data['hide'] = "none"
        elif num < session['random']:
            data['low'] = "true"
        else:
            data['high'] = "true"
    except:
        print "Not start guessing"
    print data
    return render_template("index.html", data=data, number=guess )

@app.route('/reset')
def reset():
    # session.pop('random')
    session['random'] = randint(1, 100)
    session['counter'] = 0
    print "New random: %d"%session['random']
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

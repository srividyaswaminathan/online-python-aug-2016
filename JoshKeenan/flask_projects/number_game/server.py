from flask import Flask, redirect, request, session, render_template
import random

app = Flask(__name__)
app.secret_key = 'secret squirrel'


@app.route('/', methods=['GET', 'POST'])
def index():
    data = {}
    try:
        session['number']
    except:
        session['number'] = random.randrange(0, 101)

    try:
        guess = int(request.form['guess'])
        if guess == session['number']:
            data = {'accuracy': "You Got it Right!"}
            data['color'] = 'green'
            data['correct'] = 'true'
        elif guess < session['number']:
            data = {'accuracy': 'Too low...'}
            data['color'] = 'blue'
        else:
            data = {'accuracy': 'Too high...'}
            data['color'] = 'red'
        data['guess'] = str(guess)
        print data
    except:
        data = {'accuracy': 'Make a guess!'}
        data['color'] = 'white'
        data['guess'] = 'No guesses yet!'

    return render_template('index.html', data=data)


@app.route('/reset', methods=['GET'])
def reset():
    session['number'] = random.randrange(0, 101)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

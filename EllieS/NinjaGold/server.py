from flask import Flask, session,render_template, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index ():
    if 'totalgold' not in session:
        session['totalgold'] = 0
        session['activities'] = []
    return render_template('index.html')

@app.route('/process_money', methods =['POST'])
def process_money ():
    if request.form['action'] == "farm":
        randnum = random.randint(10, 20)
        session['totalgold'] += randnum
        "You got " + str(randnum) + "From the Farm!"
    
    elif request.form['action'] == "cave":
        randnum = random.randint(5, 10)
    elif request.form['action'] == "house":
        randnum = random.randint(2, 5)
    elif request.form['action'] == "casino":
        randnum = random.randint(0, 50)

    return redirect('/')

app.run(debug=True)

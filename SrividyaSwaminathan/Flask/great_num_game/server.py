from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = "ThisIsSecretKey"

#random_number = random.randrange(0,101)

@app.route('/')
def home_page():
	if 'random_number' not in session:
		session['random_number'] = random.randrange(0, 101)
		print "I am generation", session['random_number']
	session['div'] = 'empty'
	return render_template('index.html') 

@app.route('/guess', methods=['POST'])
def guess_page():	
	guess = int(request.form['guess'])
	rnd = session['random_number']

	print "Guessed num:",guess, "randomly generated num",rnd

	if guess < rnd:		
		div_class = 'too_low'		
		div_text = "TOO LOW!"
	elif guess > rnd:		
		div_class = 'too_high'
		div_text = "TOO HIGH"
	else:
		div_class = 'solved'
		div_text = 'adad'
	session['div'] = div_class
	session['div_text'] = div_text
	return redirect('/')
@app.route('/solved', methods=['POST'])
def solved():
	session.pop('random_number')
	print "session is popped"
	return redirect('/')
app.run(debug=True)	
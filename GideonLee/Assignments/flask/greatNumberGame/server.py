from flask import Flask, render_template, session, request, redirect
from random import randrange

app = Flask(__name__) 
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'answer' not in session: 
		session['answer'] = randrange(0, 101)
		session['result'] = ''
	return render_template('index.html')

@app.route('/guess', methods=['post'])
def guess():
	#request.form makes the HTML element into a string
	session['guess'] = int(request.form['guess'])
	if session['guess'] > session['answer']:
		session['result'] = 'high'
	elif session['guess'] < session['answer']:
		session['result'] = 'low'
	else:
		session['result'] = 'exact'
	return redirect('/')

@app.route('/reset', methods=['post'])
def reset(): 
	session.pop('answer')
	return redirect('/')

app.run(debug=True)





















# from flask import Flask, render_template, session, redirect, request
# from random import randrange

# app = Flask(__name__) 
# app.secret_key = 'ThisIsSecret'

# @app.route('/')
# def index():
# 	if 'answer' not in session: 
# 		session['answer'] = randrange(1, 101)
# 		session['result'] = 'No Guess Yet'
# 	return render_template('index.html')

# @app.route('/guess', methods=['POST'])
# def guess():
# 	guess = int(request.form['guess'])
# 	if session['answer'] == guess:
# 		session['result'] = 'Spot on!'
# 	elif guess < session['answer']:
# 		session['result'] = 'TOO LOW'
# 	elif guess > session['answer']:
# 		session['result'] = 'TOO HIGH'
# 	return redirect('/')

# @app.route('/reset', methods=['POST'])
# def reset():
# 	session.pop('answer')
# 	return redirect('/')

# app.run(debug=True)



# from flask import Flask, render_template, session, redirect, request
# import random

# app = Flask(__name__) 
# app.secret_key = 'ThisIsSecret'

# @app.route('/')
# def index():
# 	session['my_target'] = random.randrange(0, 101)
# 	return render_template('index.html')

# @app.route('/tooHigh')
# def tooHigh():
# 	return render_template('tooHigh.html')

# @app.route('/tooLow')
# def tooLow():
# 	return render_template('tooLow.html')

# @app.route('/win')
# def win():
# 	return render_template('win.html')

# @app.route('/guess', methods=['POST'])
# def guess():
# 	session['guess'] = request.form['guess']
# 	my_guess = int(session['guess'])
# 	print 'Session is', session['guess']
# 	print 'Target is', session['my_target']
# 	if request.form['action'] == 'guessing':
# 		if my_guess > session['my_target']:
# 			return redirect('/tooHigh')
# 		elif my_guess < session['my_target']:
# 			return redirect('/tooLow')
# 		else: 
# 			return redirect('/win')
# 	elif request.form['action'] == 'replaying': 
# 		session.pop('guess')
# 		return redirect('/')

# app.run(debug=True)
from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ASecretKey'

@app.route('/')
def home():
	if 'rand' in session:
		session['wintest'] = ''
		if 'n' in session:
			if int(session['n']) > int(session['rand']):
				session['wintest'] = 'high'
			if int(session['n']) < int(session['rand']):
				session['wintest'] = 'low'
			if int(session['n']) == int(session['rand']):
				session['wintest'] = 'win'
				session.pop('n')
	else:
		session['rand'] = random.randrange(0,101) 
	return render_template('index.html', wintest=session['wintest'], rand=session['rand'])

@app.route('/guess', methods=['POST'])
def guess():
	session['n'] = request.form['n']
	return redirect('/')

@app.route('/reset')
def reset():
	# session.pop('wintest')
	session.pop('rand')
	session['rand'] = random.randrange(0,101)
	return redirect('/')

app.run(debug=True)


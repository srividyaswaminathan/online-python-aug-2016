from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ASecretKey'

@app.route('/')
def home():
	if 'n' in session:
		session['n'] += 1
	else :
		session['n'] = 1
	return render_template('index.html', n = session['n'])

@app.route('/plustwo')
def add():
	session['n'] += 1
	return redirect('/')

@app.route('/reset')
def reset():
	session['n'] = 0
	return redirect('/')

app.run(debug=True)
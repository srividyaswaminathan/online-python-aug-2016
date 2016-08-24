from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = "ThisIsSecretKey"

@app.route('/')
def index():
	counter = 0
	if 'counter' not in session:
		session['counter'] = 1
	session['counter'] +=1	
	return render_template('index.html')

@app.route('/ninjas', methods=['POST'])
def counter():
	return redirect('/')

@app.route('/increment', methods=['POST'])
def increment_by_2():
	if 'counter' in session:
		session['counter'] = session['counter'] + 2 #check
	
	return render_template('index.html')	
@app.route('/reset', methods=['POST'])	
def reset_to_1():
	counter = 0
	if 'counter' in session:
		session['counter'] = 1
	return redirect('index.html')
app.run(debug=True)





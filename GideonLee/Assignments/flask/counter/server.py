from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	session['counter'] += 1
	return render_template('index.html', counter=session['counter'])

# , counter=session['counter']

@app.route('/plusTwo', methods=['POST'])
def plusTwo():
	session['counter'] += 1
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['counter'] = 0
	return redirect('/')

app.run(debug=True)







 
 # Create a simple web application that holds a counter that increments every 
 # time the page is visited. Complete this using session.
 
 # For ninjas: add a +2 button underneath the counter that increments the 
 # counter by 2 and reloads the page.
 
 # For hackers: add a reset button that will reset the counter to 1
from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninjas():
	return render_template('ninja.html', ninja_color='all')

@app.route('/ninja/<ninja_color>')
def disappearing_ninja(ninja_color):
	colors = ['blue', 'purple', 'red', 'orange']
	for color in colors:
		if color == ninja_color: 
			return render_template('ninja.html', ninja_color=ninja_color)

 	return render_template('ninja.html', ninja_color='none')
app.run(debug=True)
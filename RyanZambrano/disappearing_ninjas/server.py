from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'Secret'
valid_colors = ['blue', 'orange', 'red', 'purple']


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/ninjas/')
def allNinjas():
	return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def ninjas(color):
	return render_template('ninjas.html', color=color.lower(), valid_colors=valid_colors)


app.run(debug=True)
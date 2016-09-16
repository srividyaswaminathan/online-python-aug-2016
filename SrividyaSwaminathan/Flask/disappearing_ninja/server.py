from flask import Flask, session, render_template, flash, request, redirect

app = Flask(__name__)
app.secret_key = "ThisIsASecret"

@app.route('/')
def index():
	return "No Ninjas found"

@app.route('/ninjas')
def ninjas():
	return render_template('index.html')

@app.route('/ninjas/<ninjas_color>')
def show_ninjas(ninjas_color):

	return render_template('ninjas.html', ninjas_color=ninjas_color )

app.run(debug=True)

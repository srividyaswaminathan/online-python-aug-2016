from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title='Home', description='This is the home page.')

@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html', title='Ninjas', description='This is the ninja page.')

@app.route('/dojos/new')
def dojos_new():
	return render_template('dojos/new.html', title='New Dojo Page', description='This is the dojo''s new page.')

app.run(debug=True)
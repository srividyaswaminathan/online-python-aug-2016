from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
	return render_template('index.html')
@app.route('/ninjas')
def ninjas():
	return render_template('ninja.html')
@app.route('/dojos/new')
def dojos():
	return render_template('dojos.html')

app.run(debug=True)


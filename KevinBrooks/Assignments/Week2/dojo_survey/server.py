from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['get'])
def index():
	return render_template('index.html', title='Dojo Survey', description='This is the dojo survey.')

@app.route('/', methods=['post'])
def index_post():
	return render_template('index.html', title='Dojo Survey', description='This is the dojo survey.', name=request.form['name'], location=request.form['dojo_location'], language=request.form['fav_lang'], comments=request.form['comments'])

@app.route('/result', methods=['post'])
def result():
	return render_template('result.html', title='Result Card', description='This is your result card.', name=request.form['name'], location=request.form['dojo_location'], language=request.form['fav_lang'], comments=request.form['comments'])

app.run(debug=True)
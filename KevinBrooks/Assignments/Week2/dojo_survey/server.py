from flask import Flask, render_template, request, redirect, session, flash
import random, datetime

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 

@app.route('/', methods=['get'])
def index():
	return render_template('index.html', title='Dojo Survey', description='This is the dojo survey.')

@app.route('/', methods=['post'])
def index_post():
	return render_template('index.html', title='Dojo Survey', description='This is the dojo survey.', name=request.form['name'], location=request.form['dojo_location'], language=request.form['fav_lang'], comments=request.form['comments'])

@app.route('/result', methods=['post'])
def result():
	messages = validate_fields(request.form['name'], request.form['comments'])
	if len(messages) > 0:
		for msg in messages:
			flash(msg)
		return index_post()

	return render_template('result.html', title='Result Card', description='This is your result card.', name=request.form['name'], location=request.form['dojo_location'], language=request.form['fav_lang'], comments=request.form['comments'])

def validate_fields(name, comments):
	messages = []
	if len(name.strip(' ')) < 1:
		messages.append('Please enter your name.')
	if len(comments.strip(' ')) < 1:
		messages.append('Please enter a comment.')
	if len(comments.strip(' ')) > 120:
		messages.append('Comments cannot be larger than 120 characters.')

	return messages

app.run(debug=True)
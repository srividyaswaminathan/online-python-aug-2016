from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index(): 
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def enterResults():
	name = request.form['name']
	email = request.form['email']
	location = request.form['location']
	language = request.form['language']
	comments = request.form['comments']
	return render_template('result.html', my_name=name, my_email=email, my_comments=comments, my_language=language, my_location=location)

app.run(debug=True)
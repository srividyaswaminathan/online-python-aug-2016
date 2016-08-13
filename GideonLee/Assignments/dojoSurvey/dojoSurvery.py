from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key ='ThisIsSecret'

@app.route('/')
def index(): 
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def enterResults():
	if len(request.form['name']) < 1 or len(request.form['email']) < 1 or len(request.form['comments']) < 1:
		flash('Name, email, and comments cannot be empty!')
		return redirect('/')
	if len(request.form['comments']) > 120: 
		flash('Comments cannot exceed more than 120 characters.')
		return redirect('/')
	else: 
		name = request.form['name']
		email = request.form['email']
		location = request.form['location']
		language = request.form['language']
		comments = request.form['comments']
		return render_template('result.html', my_name=name, my_email=email, my_comments=comments, my_language=language, my_location=location)

app.run(debug=True)
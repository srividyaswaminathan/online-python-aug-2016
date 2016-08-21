from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'Secret'

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():

	if len(request.form['name']) < 1 and len(request.form['comment']) < 1:
		flash("name and comment cannot be empty!")
		return redirect('/')

	elif len(request.form['name']) < 1:
		flash("name cannot be empty!")
		return redirect('/')

	elif len(request.form['comment']) < 1:
		flash("comment cannot be empty!")
		return redirect('/')
		
	return render_template('result.html',
		name=request.form['name'],
		location=request.form['location'],
		language=request.form['language'],
		comment=request.form['comment']
		)

app.run(debug=True)
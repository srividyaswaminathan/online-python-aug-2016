from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 

@app.route('/', methods=['get'])
def index():
	session['answer'] = random.randrange(1,101)
	return render_template('index.html', replay_visible='none', guess_visible='block', feedback_visible='none')		

@app.route('/', methods=['post'])
def index_post():
	if request.form['btn_submit'] is not None:
		try:
			guess = int(request.form['txt_guess'])
		except:
			guess = -1
	
		answer = int(session['answer'])
		if guess == answer:
			return render_template('index.html', number=answer, replay_visible='block', guess_visible='none', feedback_visible='none')			
		elif guess > answer:
			return render_template('index.html', replay_visible='none', guess_visible='block', feedback_visible='block', high_low='high')		
		else:
			return render_template('index.html', replay_visible='none', guess_visible='block', feedback_visible='block', high_low='low')		
	else:
		return render_template('index.html', replay_visible='none', guess_visible='block', feedback_visible='none')	
	

app.run(debug=True)
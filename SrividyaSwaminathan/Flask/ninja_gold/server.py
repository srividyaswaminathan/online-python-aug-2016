from flask import Flask, render_template, redirect, session, request
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "ThisIsSecretKeyAB"

@app.route('/')
def home_page():
	if 'gold_count' not in session:
		session['gold_count'] = 0
		session['activity'] = []

	return render_template('index.html') 

@app.route('/process_money', methods=['POST'])
def find_gold():
	building = request.form['building']
	print "visiting : ", building

	
	if building == 'farm':
		coins = random.randrange(10,21)		
	elif building == 'cave':
		coins = random.randrange(5,11)		
	elif building == 'house':
		coins = random.randrange(2,6)		
	else:
		coins = random.randrange(-50,51)
		
	if coins > 0:
		activity = 'Earned %d coins from the %s!' % (coins, building)
	elif coins < 0:
		activity = 'Entered a casino and lost %d golds... Ouch...' % (abs(coins))
	else:
		activity = 'Entered a casino and exited without any profit or loss' 

	current_date = datetime.now()
	activity = '%s (%s)' % (activity, current_date)

	print "Coins", coins
	print "activity", activity
	
	session['gold_count'] += coins
	session['activity'].append(activity)

	return redirect('/')


@app.route('/reset')	
def reset():
	session.pop('gold_count')	
	return redirect('/')

app.run(debug=True)

from flask import Flask, render_template, session, request, redirect
from random import randrange
import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'gold' not in session: 
		session['gold'] = 0
		session['counter'] = 0
		session['list'] = []
		session['text_color'] = []
	return render_template('index.html')

@app.route('/process_money', methods=['post'])
def process():
	#Format the current date
	date = datetime.datetime.now()
	ampm = 'am'
	hour = str(getattr(date, 'hour'))

	#Change 24 hr time to 12 hr time
	if getattr(date, 'hour') > 12:
		hour = str(getattr(date, 'hour') - 12)
		ampm = 'pm'
	#If minutes is less than one digit, add a '0' to the front
	minute = str(getattr(date, 'minute'))
	if getattr(date, 'minute') < 10:
		minute = '0' + minute
	#If month is less than one digit, add a '0' to the front
	month = str(getattr(date, 'month')) 
	if getattr(date, 'month') < 10:
		month = '0' + month
	#if date is less than one digit, add a '0' to the front 
	day = str(getattr(date, 'day'))
	if getattr(date, 'day') == 8:
		day = '0' + day

	#Current date and time 
	time = '('+ str(getattr(date, 'year')) + '/' + month + '/' + day +  ' - ' + hour + ':' + minute + ' ' + ampm + ')'
	
	#Generate gold earning
	session['option'] = request.form['building']
	if session['option'] == 'farm':
		session['earnings'] = randrange(10, 21)
		location = 'farm'
		session['text_color'].append('green')
	elif session['option']== 'cave':
		session['earnings'] = randrange(5, 11)
		location = 'cave'
		session['text_color'].append('green')
	elif session['option'] == 'house':
		session['earnings'] = randrange(2, 6)
		location = 'house' 
		session['text_color'].append('green')
	elif session['option'] == 'casino':
		session['earnings'] = randrange(-50, 50)
		location = 'casino'
		if session['earnings'] >= 0:
			session['text_color'].append('green')
		elif session['earnings'] < 0:
			session['text_color'].append('red')

	#Create a counter to track how many elements are inside the list of earnings
	session['counter'] += 1
	
	#Push these values into a list for the activity log
	if location == 'casino' and session['earnings'] > 0:
		session['list'].append('Entered a casino and won ' + str(session['earnings']) + ' gold!' + ' ' + time)
	elif location =='casino' and session['earnings'] < 0:
		session['list'].append('Entered a casino and lost ' + str(session['earnings']) + ' gold ... ouch... ' + time)
	else: 
		session['list'].append('Earned ' + str(session['earnings']) + ' from the ' + location + ' ' + time)

	#Update the total gold earnings value 
	session['gold'] += session['earnings']
	return redirect('/')

@app.route('/reset', methods=['post'])
def reset():
	#gets rid of all the sessions
	session.clear()
	return redirect('/')
app.run(debug=True)
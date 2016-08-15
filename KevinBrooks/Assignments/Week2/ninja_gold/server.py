from flask import Flask, render_template, request, redirect, session
import random, datetime

app = Flask(__name__)
app.secret_key = 'ADF2B64D-D02D-484F-BBA6-324C16CF457F' 

@app.route('/', methods=['get'])
def index():
	print ('hey')
	if not session.get('gold'):
		session['gold'] = 0
		session['activities'] = []

	html = get_activity_html(session['activities'])	
	return render_template('index.html', gold=session['gold'], activities=html)

@app.route('/process_money', methods=['post'])
def index_post():
	pricing = { 'farm': (10, 20), 'cave': (5,10), 'house': (2,5),  'casino': (-50,50)}
	key = request.form.keys()[0]
	activities = session['activities']
	msg = '{0} {1} gold {2}. {3}'
	gold_earned = random.randrange(pricing[key][0], pricing[key][1])
	session['gold'] = int(session['gold']) + gold_earned
	date = datetime.datetime.now()
	msg_from = ('from the ' + key, '.....ouch....')[gold_earned < 0]
	msg_verb = ('Earned', 'Entered the casino and lost')[gold_earned < 0]
	show_green = msg_verb == 'Earned' 
	if gold_earned < 0:
		gold_earned = gold_earned * -1
	msg = msg.format( msg_verb, gold_earned , msg_from, date)
	activities.append((show_green,msg))
	return redirect('/')	

def get_activity_html(activities):
	if len(activities) == 0:
		return ''

	html = "<p style='color: {0};'>{1}</p>"
	result = ''
	for i in range(len(activities)):
		color = 'green'
		if not activities[i][0]:
			color = 'red'
		result += html.format(color, activities[i][1])
	else:
		pass

	return result
	

app.run(debug=True)
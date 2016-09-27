from django.shortcuts import render, HttpResponse, redirect
import random, datetime

# Create your views here.

def index(request):
	ensure_session(request)
	html = get_activity_html(request.session['activities'])
	context = {
		'activities' : html,
		'gold': request.session['gold']
	}
	return render(request, 'ninja_gold/index.html', context)

def process_money(request):
	if request.method == 'GET':
		return redirect('/')

	ensure_session(request)
	pricing = { 'farm': (10, 20), 'cave': (5,10), 'house': (2,5),  'casino': (-50,50)}
	key = get_action_key(request.POST)
	activities = request.session['activities']
	msg = '{0} {1} gold {2}. {3}'
	gold_earned = random.randrange(pricing[key][0], pricing[key][1])
	request.session['gold'] = int(request.session['gold']) + gold_earned
	date = datetime.datetime.now()
	msg_from = ('from the ' + key, '.....ouch....')[gold_earned < 0]
	msg_verb = ('Earned', 'Entered the casino and lost')[gold_earned < 0]
	show_green = msg_verb == 'Earned' 
	if gold_earned < 0:
		gold_earned = gold_earned * -1
	msg = msg.format( msg_verb, gold_earned , msg_from, date)
	activities.append((show_green,msg))

	return redirect('/')

def ensure_session(request):
	if not 'activities' in request.session:
		request.session['activities'] = []
		request.session['gold'] = 0

	return True

def get_action_key(form):
	if 'house' in form:
		return 'house'
	if 'farm' in form:
		return 'farm'
	if 'cave' in form:
		return 'cave'
	if 'casino' in form:
		return 'casino'

	return ''

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
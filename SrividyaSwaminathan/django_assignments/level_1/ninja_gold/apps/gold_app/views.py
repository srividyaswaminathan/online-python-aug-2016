from django.shortcuts import render, redirect
import random
from datetime import datetime
# Create your views here.
def index(request):
	if 'gold_count' not in request.session or 'activity' not in request.session:
		request.session['gold_count'] = 0
		request.session['activity'] = []
	context = {
				'activities': request.session['activity'],
				'gold_count': request.session['gold_count']
	}
	
	print "acts = ", context
	return render(request, 'gold_app/index.html', context)

def find_gold(request):
	if request.method == "POST":
		building = request.POST['building']
		print "visiting : ", building
	  	if building == 'farm':
			coins = random.randrange(10,21)		
		elif building == 'cave':
			coins = random.randrange(5,11)		
		elif building == 'house':
			coins = random.randrange(2,6)		
		else:
			coins = random.randrange(-50,51)
     	
	current_date = str(datetime.now())
	if coins > 0:
		activity = ('Earned %d coins from the %s!' % (coins, building), 'gain', current_date)
	elif coins < 0:
		activity = ('Entered a casino and lost %d golds... Ouch...' % (abs(coins)), 'loss', current_date)
	else:
		activity = ('Entered a casino and exited without any profit or loss', 'same', current_date)

	
	print "Coins", coins
	print "activity", activity
	request.session['gold_count'] += coins
	request.session['activity'].append(activity)


	return redirect('/')	
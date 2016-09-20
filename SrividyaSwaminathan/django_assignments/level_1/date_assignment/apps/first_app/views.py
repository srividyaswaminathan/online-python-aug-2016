from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
	current_time = datetime.now()
	print "current time is", current_time
	date_time = {
					'date_time': current_time
	}
	return render(request, "first_app/index.html", date_time)

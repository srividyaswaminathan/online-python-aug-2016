from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    date = datetime.datetime.now()
    data = {
	    "date": date.strftime('%B %d, %Y'),
	    "time": date.strftime('%I:%M %p')
    }
    return render(request,'timedisplay/index.html', data)

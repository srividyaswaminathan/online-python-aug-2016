from django.shortcuts import render, redirect

import random
import string
# Create your views here.
def random_word_generator(size, random_string = string.ascii_uppercase + string.digits):
	return ''.join(random.choice(random_string) for _ in range(size))

def index(request):
	print "this is the views file"
	return render(request, 'first_app/index.html')


def show(request):
	random = random_word_generator(13, string.ascii_uppercase + string.digits)
	request.session['random'] = random
	print random
	if request.method == "POST":
		print request.POST
		return render(request, 'first_app/show.html')	

	else:
		return redirect('/')	

from django.shortcuts import render, redirect
import random, string

def get_random_word(length):
   return ''.join(random.choice(string.lowercase) for i in range(length))

# Create your views here.

def index(request):
	try:
		context = {'attempts' : request.session['attempts'], 'new_word' : request.session['new_word']}
	except Exception, e:
		context = {'attempts' : 0, 'new_word' : ''}
	else:
		pass
	finally:
		pass	

	return render(request, 'word_gen/index.html', context)

def new_word(request):
	if not 'attempts' in request.session:
		request.session['attempts'] = 0

	if request.method == 'POST':
		word = get_random_word(14)
		request.session['attempts'] += 1
		request.session['new_word'] = word

	return redirect('/')

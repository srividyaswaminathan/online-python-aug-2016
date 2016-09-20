from django.shortcuts import render, redirect

# Create your views here.

def index(request):
	if request.method == 'POST':
		context = {
			'name' : request.session['name'],
			'dojo' : request.session['dojo'],
			'lang' : request.session['lang'],
			'comment' : request.session['comment']
		}
		return render(request, 'survey/index.html', context)
	else:
		return render(request, 'survey/index.html')

def process_survey(request):
	if request.method == 'GET':
		return redirect('/')

	if not 'submissions' in request.session:
		request.session['submissions'] = 0

	request.session['submissions'] += 1
	request.session['name'] = request.POST['name']
	request.session['dojo'] = request.POST['dojo']
	request.session['lang'] = request.POST['lang']
	request.session['comment'] = request.POST['comment']

	return redirect('/result')

def result(request):
	try:
		context = {
			'submissions' : request.session['submissions'],
			'name' : request.session['name'],
			'dojo' : request.session['dojo'],
			'lang' : request.session['lang'],
			'comment' : request.session['comment']
		}
	except Exception, e:
		redirect('/')
	else:
		pass
	finally:
		pass	
	
	return render(request, 'survey/result.html', context)	
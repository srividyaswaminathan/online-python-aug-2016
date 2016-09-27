from django.shortcuts import render,HttpResponse, redirect

# Create your views here.

def index(request):
	return render(request, 'ninjas/index.html')

def view_ninja(request, color):
	color_map = {
		'blue' : '/static/ninjas/img/ninjas/leonardo.jpg',
		'orange' : '/static/ninjas/img/ninjas/michelangelo.jpg',
		'red' : '/static/ninjas/img/ninjas/raphael.jpg',
		'purple' : '/static/ninjas/img/ninjas/donatello.jpg',
		'ninjas' : '/static/ninjas/img/ninjas/tmnt.png',
		'hack' : '/static/ninjas/img/ninjas/notapril.jpg'
	}

	try:
		context = { 'pic' : color_map[color] }
	except Exception, e:
		context = { 'pic' : color_map['hack'] }
	else:
		pass
	finally:
		pass
	
	return render(request, 'ninjas/ninja.html', context)

def view_all(request):
	color='ninjas'
	return view_ninja(request, color)
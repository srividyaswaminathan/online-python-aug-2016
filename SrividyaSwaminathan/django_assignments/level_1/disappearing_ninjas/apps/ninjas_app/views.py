from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'ninjas_app/index.html') 

def show(request):
	return render(request, 'ninjas_app/show.html') 	

def ninjas(request, ninjas_color):
	
	context = {
				'ninjas_color': ninjas_color
	}
	return render(request, 'ninjas_app/ninjas.html', context) 		
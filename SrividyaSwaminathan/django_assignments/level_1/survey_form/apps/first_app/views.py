from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	print "this is the views file"
	return render(request, 'first_app/index.html')

def process(request):
	#show the result of inputting data in the form to /results
	print "function show"
	first_name = request.POST['first_name']  
	location = request.POST['location'] 
	language = request.POST['language'] 
	comment = request.POST['comment'] 
	
	if request.method == "POST":
		request.session['name'] = first_name
		request.session['location'] = location
		request.session['language'] = language
		request.session['comment'] = comment
		 
		if 'count' in request.session:
	 		request.session['count'] +=1
		else:
	 		request.session['count'] = 1 	
		return redirect('/results')
	else:
	   return redirect('/')    

def show(request):
	return render(request, 'first_app/show.html')
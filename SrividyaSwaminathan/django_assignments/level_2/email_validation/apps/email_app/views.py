from django.shortcuts import render, redirect
from .models import Email
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request, 'email_app/index.html')

def process_email(request):
	#insert into data base after validations
	print (request.method)
	if request.method == "POST":
		result_tuple = Email.objects.email_validation(email=request.POST['email'])
		if result_tuple[0]:
			messages.info(request, 'Email address you have entered is valid')
			return redirect('/show_email')
		if not result_tuple[0]:
			messages.info(request, 'Email Id is not valid')
			return render(request, 'email_app/index.html')	
def show_email(request):
	#show emails 
	context = {
				'emails': Email.objects.all() #runs the select * from emails
	}
	return render(request, 'email_app/show.html', context)

def destroy(request, id):
	#delete email from database
	Email.objects.get(id=id).delete()
	return redirect('/show_email')
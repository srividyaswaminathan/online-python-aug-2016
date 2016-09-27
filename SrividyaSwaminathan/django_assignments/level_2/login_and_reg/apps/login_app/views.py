from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request, 'login_app/index.html')

def success(request):
	return render(request, 'login_app/success.html')

def login(request):
	if request.method == "POST":
		result = User.objects.login_validation(email=request.POST['email'], password=request.POST['password'])
		if result[0]:
			request.session['first_name'] = result[1]
			messages.info(request, 'Welcome to the login page!!')
			return redirect('/success')
		else:
			messages.info(request, 'Email address and password you have entered does not match')
			return redirect('/')	

def register(request):
	print (request.method)
	if request.method == "POST":
		result_tuple = User.objects.registration_validation(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'], c_password=request.POST['c_password'])
		if result_tuple[0]:
			messages.info(request, 'Thank you for registering with us!')
			return redirect('/success')
		else:
			messages.info(request, result_tuple[1])  #ask how to return error list
			return redirect('/')	



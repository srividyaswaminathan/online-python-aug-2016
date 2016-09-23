from django.shortcuts import render
from .models import Course, Description
# Create your views here.
def index(request):
	context ={
				'course_name': Course.objects.all(),
				'content': Description.objects.all()
	}
	return render(request, 'course_app/index.html', context)

def insert(request):
	#validations for name and description
	request.POST['course_name'] = course_name
	request.POST['content']= content
		#insert the name, description into DB
	valid_fields = True	
	if len(course_name)<2:
		valid_fields= False
	if len(content)<2:
		valid_fields= False		
	if valid_fields:
		#creates a query to insert into
		Description.objects.create(course__name=request.POST['course_name'], content=request.POST['content'])
	return redirect('/')

def show(request):
	pass

def delete(request):
	pass		

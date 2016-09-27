from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Course
# Create your views here.
def index(request):
	#render index html page and show all courses
	context = {
	            'show_all_courses': Course.objects.all(),
	}
	return render(request, 'courses_app/index.html', context)

def add_course(request):
	#use create() to add a couorse to the DB
	if request.method=="POST":
		add_course = Course.objects.create(name=request.POST['course_name'], description=request.POST['course_description']) #binding variable used on left side shld be taken on template
		print add_course
		print request.POST
		return redirect(reverse('index'))

def destroy(request, id):
	#use delete method to delete
	course_to_delete = Course.objects.get(id=id)
	if request.method=="GET":
		#render a template that shows if the course can be deleted
		context = { 
					'course_to_delete': course_to_delete,
		   }
		return render(request, 'courses_app/confirm_delete.html', context)
	if request.method=="POST":
		course_to_delete.delete()	
		return redirect(reverse('index'))
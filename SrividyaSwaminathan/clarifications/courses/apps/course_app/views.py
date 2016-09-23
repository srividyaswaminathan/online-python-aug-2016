from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'course_app/index.html')


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
		#ask how to insert in DB
		context = {
					'course_name': course_name,
					'content': content
		}
		return render(request, 'course_app/index.html', context)

def show(request):
	pass

def delete(request):
	pass		

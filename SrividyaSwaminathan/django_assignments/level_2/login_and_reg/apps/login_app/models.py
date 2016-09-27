from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
# Create your models here.
#write login and user manager
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
	def registration_validation(self, **kwargs):
		error_list = []
		#declaring variables
		first_name = kwargs['first_name']  
		last_name = kwargs['last_name'] 
		email = kwargs['email']
		password = kwargs['password']
		c_password = kwargs['c_password'] 
		valid_fields = True
		print "keyword arguments", kwargs
		#validate first name and last name
		if len(first_name)<2:
			error_list.append("First name should be more than 2 characters in length")
			valid_fields = False
		if not first_name.isalpha():
			error_list.append("First name can contain letters only")
			valid_fields = False
		if len(last_name)<2:
			error_list.append("Last name should be more than 2 characters in length")
			valid_fields = False
		if not last_name.isalpha():
			error_list.append("Last name can contain letters only")	
			valid_fields = False
		#validate email 
		if not EMAIL_REGEX.match(email):
			error_list.append("Please enter a valid email")
			valid_fields = False
		#validate password using Bcrypt
		if password != c_password:
			error_list.append("Passwords do not match")
			valid_fields = False
		if not valid_fields:
			print "error list ", error_list
			return (False, error_list)
		else:
			hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
			print hashed
			result = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed)	
			return (True, result)

	def login_validation(self, **kwargs):
		#email and password validate for that particular user
		req_email = kwargs['email']
		req_password = kwargs['password']
		#The email typed should match the email of particular user. This can be done by using .get with user name
		user_in_db = User.objects.get(email=req_email)
		#get the password for the email object from db req_password
		hashed_password_in_db = user_in_db.password

		if bcrypt.hashpw(req_password.encode(), hashed_password_in_db.encode()) == hashed_password_in_db:
			print "It matches"
			return (True, user_in_db.first_name)
		else:
			print "It does not match"
			return (False, "Email and password did not match")

class User(models.Model):	
	first_name = models.CharField(max_length=255) 
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	
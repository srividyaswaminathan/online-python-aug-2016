from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class EmailManager(models.Manager):
	def email_validation(self, **kwargs):
		# add validations for email here
		error_list = []
		print "key word arguments passed are", kwargs
		print "*" * 50
		email = kwargs['email']
		if not EMAIL_REGEX.match(email):
			error_list.append("Please enter a valid email address")
			print error_list
			return (False, error_list)
		else:
			result = Email.objects.create(email=email) 
			print result #keyword passed here on left side should match the table name in the database
			return (True, result) 		

class Email(models.Model):
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True) 
	updated_at = models.DateTimeField(auto_now=True)
	objects = EmailManager()

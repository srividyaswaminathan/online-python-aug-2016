from __future__ import unicode_literals
from django.db import models
# Create your models here.
class User(models.Model):
	first_name= models.CharField(max_length= 75)
	last_name= models.CharField(max_length= 75)
	email= models.EmailField()
	password= models.CharField(max_length= 100)
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)

class Message(models.Model):
	message= models.TextField(max_length= 1000)
	user_id = models.ForeignKey(User)
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)	

class Comment(models.Model):
	comment= models.TextField(max_length= 1000)
	message_id= models.ForeignKey(Message)
	user_id= models.ForeignKey(User)
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)	




from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=255) 
	product_description = models.TextField(max_length=255)
	product_price = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
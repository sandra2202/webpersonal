from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=200)   
	description = models.TextField()   
	image = models.ImageField()   
	created = models.DateTimeField(auto_now_add=True,)   
	update = models.DateTimeField(auto_now=True)   
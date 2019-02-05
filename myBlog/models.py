from django.db import models

# Create your models here.
class post(models.Model):
	title = models.CharField(max_length=140)
	body = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title

	

class author(models.Model):
	name = models.CharField(max_length=50)
	pic = models.ImageField()

	def __str__(self):
		return self.name
				
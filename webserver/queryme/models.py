from django.db import models

# Create your models here.
class Log(models.Model):
	timestamp = models.DateTimeField()
	action_type = models.CharField(max_length=200)
	action_content = models.CharField(max_length=200)
	userip = models.CharField(max_length=200)
	
	def __str__(self):
		return self.timestamp + " " + self.userip + " " + self.action_type + " " + self.action_content
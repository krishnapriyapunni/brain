from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class UserProfile(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,)
	email=models.EmailField()
	password=models.CharField(max_length=30)
	mobile=models.CharField(max_length=10)
    # appoinment=models.


	def __str__(self):
		return str(self.user.username)


class Document(models.Model):
   
    document = models.FileField(upload_to='documents/')
    
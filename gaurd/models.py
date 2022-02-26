from django.db import models

# Create your models here.
class gaurd_data(models.Model):    
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    DOJ = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
   
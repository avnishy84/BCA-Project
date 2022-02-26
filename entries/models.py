from django.db import models

# Create your models here.
class entry_data(models.Model):
    date = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    entrytime = models.CharField(max_length=100)
    exittime = models.CharField(max_length=100)
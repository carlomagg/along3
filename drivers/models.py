from django.db import models

# Create your models here.

class Drivers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone= models.CharField(max_length=11)
    address =models.CharField(max_length=100)
    license = models.CharField(max_length=100)
    
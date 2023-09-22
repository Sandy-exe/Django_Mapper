from django.db import models

# Create your models here.

class Product(models.Model):
    type = models.CharField(max_length=100)
    make = models.CharField(max_length=120)
    model = models.CharField(max_length=100)
    price = models.IntegerField()

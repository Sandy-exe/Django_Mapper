from django.db import models

# Create your models here.

class Product(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()

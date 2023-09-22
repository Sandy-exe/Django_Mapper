from django.db import models

# Create your models here.

class Product(models.Model):
    type = models.CharField(max_length=100)
    make = models.CharField(max_length=120)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
class EWaste_facility(models.Model):
    EWaste_facility_name = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.EWaste_facility_name
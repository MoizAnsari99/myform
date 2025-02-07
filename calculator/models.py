from django.db import models

# Create your models here.
class bike_EF(models.Model):
    Engine_cc = models.IntegerField()
    kg_per_km = models.FloatField()

class car_EF(models.Model):
    Engine_cc = models.IntegerField()
    kg_per_km = models.FloatField()
    Engine_cc = models.IntegerField()
    type_of_car = models.CharField(max_length=200)

class bus_EF(models.Model):
    type_of_bus = models.CharField(max_length=200)
    kg_per_km = models.FloatField()

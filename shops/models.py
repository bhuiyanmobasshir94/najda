from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
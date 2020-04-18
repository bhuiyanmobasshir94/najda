from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Needy(models.Model):
    location_name = models.CharField(max_length=255) # editable by people
    introducer_name = models.CharField(max_length=255, null= True, blank=True)
    introducer_number = PhoneNumberField(null= True, blank=True)
    message = models.TextField()
    people_count = models.IntegerField()
    priority = models.IntegerField()
    location = models.PointField()
    city = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location_name
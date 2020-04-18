from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import Needy

@admin.register(Needy)
class NeedyAdmin(OSMGeoAdmin): 
    search_fields = ['location_name','people_count','priority','area','city']
    list_filter = ['location_name','people_count','priority','area','city','created_on']   
    list_display = ('location_name','introducer_name','introducer_number','people_count','priority','area','city','created_on')
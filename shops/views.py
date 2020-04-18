from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

latitude = 23.71600823152872
longitude = 90.41680990389672

user_location = Point(longitude, latitude, srid=4326)

def measurement_conversion(value,unit):
    if str(unit) == "mi":
        return value * 1609.344
    elif str(unit) == "km":
        return value * 1000.0
    else:
        return value * 1.0


class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',user_location)).filter(distance__lte= measurement_conversion(2,"mi")).order_by('distance')
    template_name = 'shops/index.html'
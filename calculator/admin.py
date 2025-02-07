from django.contrib import admin
from .models import bike_EF, car_EF, bus_EF

# Register your models here.
admin.site.register(bike_EF)
admin.site.register(car_EF)
admin.site.register(bus_EF)
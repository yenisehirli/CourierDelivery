from django.contrib import admin
from .models import User, CourierVehicle, NavigationRecord,Client,Order

admin.site.register(User)
admin.site.register(CourierVehicle)
admin.site.register(NavigationRecord)
admin.site.register(Client)
admin.site.register(Order)


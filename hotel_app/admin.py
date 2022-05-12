from django.contrib import admin
from .models import *;

admin.site.register(Rooms)
admin.site.register(Guests)
admin.site.register(Reservations)
admin.site.register(Service)
admin.site.register(Service_group)


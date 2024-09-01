from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cities)
admin.site.register(Trains)
admin.site.register(TrainRoutes)
admin.site.register(Tickets)
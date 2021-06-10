from django.contrib import admin
#
from .models import CityModel, HistoryModel

# Register your models here.


admin.site.register(CityModel)
admin.site.register(HistoryModel)

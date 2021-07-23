from django.contrib import admin
#
from . import models

# Register your models here.

admin.site.register(models.PhoneLapModel)
admin.site.register(models.TypeModel)
admin.site.register(models.VidPicModel)
admin.site.register(models.OrderModel)

from django.contrib import admin
#
from . import models

# Register your models here.

admin.site.register(models.RoomModel)
admin.site.register(models.RoomUserModel)
admin.site.register(models.MessageModel)
admin.site.register(models.VidPicModel)
admin.site.register(models.LikeModel)
admin.site.register(models.TimelineModel)

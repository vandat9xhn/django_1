from django.contrib import admin
#
from . import models

# Register your models here.


all_models = [
    models.FriendModel, models.AddFriendModel
]

#
for model in all_models:
    admin.site.register(model)

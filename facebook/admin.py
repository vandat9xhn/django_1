from django.contrib import admin
#
from .child_app.post.admin import all_models

# Register your models here.


#
for model in all_models:
    admin.site.register(model)
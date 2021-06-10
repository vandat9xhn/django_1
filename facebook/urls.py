from django.urls import path
#
from .child_app.urls import urlpatterns as app_urls

#


urlpatterns = [
    *app_urls,
]

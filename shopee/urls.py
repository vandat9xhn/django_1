from django.urls import path
#
from .child_app.urls import urlpatterns as child_urls

#


urlpatterns = [
    *child_urls,
]

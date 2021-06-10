# from django.urls import path
#
from .post.urls import urlpatterns as post_urls

#


urlpatterns = [
    *post_urls,
]

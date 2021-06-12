from django.urls import path
#
from . import views

#


urlpatterns = [
    path('like-lc/', views.LikeViewLC.as_view()),
    path('share-lc/', views.ShareViewLC.as_view()),
]

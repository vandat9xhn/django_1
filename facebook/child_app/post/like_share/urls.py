from django.urls import path
#
from .views import LikeViewL, ShareViewL

#


urlpatterns = [
    path('like-l/', LikeViewL.as_view()),
    path('share-l/', ShareViewL.as_view()),
]

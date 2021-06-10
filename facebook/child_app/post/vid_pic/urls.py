from django.urls import path
#
from .views import VidPicViewL, VidPicLikeViewL, VidPicShareViewL
#
from .comment.urls import urlpatterns as cmt_urls

#


urlpatterns = [
    path('vid-pic-l', VidPicViewL.as_view()),
    path('vid-pic-like-l', VidPicLikeViewL.as_view()),
    path('vid-pic-share-l', VidPicShareViewL.as_view()),
    *cmt_urls,
]

from django.urls import path
#
from . import views
#
from .comment.urls import urlpatterns as cmt_urls

#


urlpatterns = [
    path('vid-pic-l', views.VidPicViewL.as_view()),
    path('vid-pic-rud', views.VidPicViewRUD.as_view()),

    path('vid-pic-like-lc', views.VidPicLikeViewLC.as_view()),
    path('vid-pic-share-lc', views.VidPicShareViewLC.as_view()),

    path('vid-pic-history-l', views.VidPicHistoryViewL.as_view()),

    *cmt_urls,
]

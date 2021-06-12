from django.urls import path
#
from . import views
#
from .sub.urls import urlpatterns as sub_urls

#


urlpatterns = [
    path('vid-pic-cmt-lc/', views.VidPicCmtViewLC.as_view()),
    path('vid-pic-cmt-ud/<int:pk>/', views.VidPicCmtViewUD.as_view()),

    path('vid-pic-cmt-like-lc/', views.VidPicCmtLikeViewLC.as_view()),

    path('vid-pic-cmt-his-l/', views.VidPicCmtHistoryViewL.as_view()),

    *sub_urls,
]

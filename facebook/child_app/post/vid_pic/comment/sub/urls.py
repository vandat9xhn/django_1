from django.urls import path
#
from . import views

#


urlpatterns = [
    path('vid-pic-sub-lc/', views.VidPicSubViewLC.as_view()),
    path('vid-pic-sub-ud/<int:pk>/', views.VidPicSubViewUD.as_view()),

    path('vid-pic-sub-like-lc/', views.VidPicSubLikeViewLC.as_view()),

    path('vid-pic-sub-his-l/', views.VidPicSubHistoryViewL.as_view()),
]

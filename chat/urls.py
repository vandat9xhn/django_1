from django.urls import path
#
from . import views

#


urlpatterns = [
    path('room-l/', views.RoomViewL.as_view()),
    path('room-count/', views.RoomCountView.as_view()),
    path('room-r/<slug:room_chat>/', views.RoomViewR.as_view()),
    # path('room-u/<slug:room_chat>/'),

    path('time-line-lc/', views.TimelineViewL.as_view()),
    path('message-lc/', views.MessageViewLC.as_view()),
    path('message-vid-pic-l/', views.VidPicViewL.as_view()),
    path('message-like-l/', views.LikeViewL.as_view()),
]

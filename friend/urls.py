from django.urls import path
#
from . import views

#


urlpatterns = [
    path('friend-may-know-l/', views.FriendMayKnowViewL.as_view()),
    path('friend-lc/', views.FriendViewLC.as_view()),
    path('friend-d/<int:pk>/', views.FriendViewD.as_view()),

    path('add-friend-lc/', views.AddFriendViewLC.as_view()),
    path('add-friend-d/<int:pk>/', views.AddFriendViewD.as_view()),
]

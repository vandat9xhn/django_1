from django.urls import path
#
from . import views

#


urlpatterns = [
    path('about/you-u/', views.AboutYouViewU.as_view()),
    path('about/hobby-u/', views.HobbyViewU.as_view()),

    path('about/other-name-c/', views.OtherNameViewC.as_view()),
    path('about/other-name-ud/<int:pk>/', views.OtherNameViewUD.as_view()),
]

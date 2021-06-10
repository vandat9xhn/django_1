from django.urls import path
#
from . import views

#


urlpatterns = [
    path('about/life-event-c/', views.LifeEventViewC.as_view()),
    path('about/life-event-ud/<int:pk>/', views.LifeEventViewUD.as_view()),
]

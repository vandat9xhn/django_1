from django.urls import path
#
from . import views

#


urlpatterns = [
    path('about/town-c/', views.TownViewC.as_view()),
    path('about/town-ud/<int:pk>/', views.TownViewUD.as_view()),

    path('about/city-c/', views.CityViewC.as_view()),
    path('about/city-ud/<int:pk>/', views.CityViewUD.as_view()),
]

from django.urls import path
#
from . import views

#


urlpatterns = [
    path('city-l/', views.CityViewL.as_view()),
    path('city-no-token-l/', views.CityViewNoTokenL.as_view()),
    path('city-c/', views.CityViewC.as_view()),
    path('city-u/<int:pk>/', views.CityViewU.as_view()),
    path('city-d/<int:pk>/', views.CityViewD.as_view()),

    path('history-l/', views.HistoryViewL.as_view()),
]

from django.urls import path
#
from . import views

#


urlpatterns = [
    path('about/gender-u/', views.GenderViewU.as_view()),
    path('about/birth-u/', views.BirthViewU.as_view()),
    path('about/language-u/', views.LanguageViewU.as_view()),
]

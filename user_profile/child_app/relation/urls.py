from django.urls import path
#
from . import views

#


urlpatterns = [
    path('about/relation-u/', views.RelationViewU.as_view()),

    path('about/family-c/', views.FamilyViewC.as_view()),
    path('about/family-ud/<int:pk>/', views.FamilyViewUD.as_view()),
]

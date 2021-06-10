from django.urls import path
#
from . import views

#


urlpatterns = [
    path('about/work-c/', views.WorkViewC.as_view()),
    path('about/work-ud/<int:pk>/', views.WorkViewUD.as_view()),

    path('about/school-c/', views.SchoolViewC.as_view()),
    path('about/school-ud/<int:pk>/', views.SchoolViewUD.as_view()),

    path('about/university-c/', views.UniversityViewC.as_view()),
    path('about/university-ud/<int:pk>/', views.UniversityViewUD.as_view()),
]

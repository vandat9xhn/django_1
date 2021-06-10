from django.urls import path
#
from . import views

#


urlpatterns = [
    path('about/picture-l/', views.PictureViewL.as_view()),
    path('about/picture-UD/<int:pk>/', views.PictureViewUD.as_view()),

    path('about/cover-l/', views.CoverViewL.as_view()),
    path('about/cover-UD/<int:pk>/', views.CoverViewUD.as_view()),
]

from django.urls import path
#
from . import views

#


urlpatterns = [
    path('notice-count-new/', views.NoticeCountNewView.as_view()),
    path('notice-l/', views.NoticeViewL.as_view()),
    path('notice-u/<int:pk>/', views.NoticeViewU.as_view()),
]

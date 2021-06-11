from django.urls import path
#
from . import views

#

urlpatterns = [
    path('transport-l/', views.TransportViewL.as_view()),
]

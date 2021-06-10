from django.urls import path
#
from .views import TransportViewL

#

urlpatterns = [
    path('transport-l/', TransportViewL.as_view()),
]

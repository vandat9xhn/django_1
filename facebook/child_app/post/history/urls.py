from django.urls import path
#
from .views import HistoryViewL
#


#


urlpatterns = [
    path('history/', HistoryViewL.as_view()),
]

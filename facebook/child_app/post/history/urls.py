from django.urls import path
#
from . import views
#


#


urlpatterns = [
    path('history-l/', views.HistoryViewL.as_view()),
]

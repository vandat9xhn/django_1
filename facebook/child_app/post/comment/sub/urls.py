from django.urls import path
#
from . import views

#


urlpatterns = [
    path('sub-lc/', views.SubViewLC.as_view()),
    path('sub-ud/<int:pk>/', views.SubViewUD.as_view()),

    path('sub-like-lc/', views.SubLikeViewLC.as_view()),

    path('sub-his-l/', views.SubHistoryViewL.as_view()),
]

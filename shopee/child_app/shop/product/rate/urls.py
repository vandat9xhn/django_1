from django.urls import path
#
from . import views

#

urlpatterns = [
    path('product-rate-l/', views.ProductRateViewL.as_view()),
]

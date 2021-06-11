from django.urls import path
#
from . import views

#

urlpatterns = [
    path('product-rate-l/', views.ProductRateViewL.as_view()),
    path('product-rate-no-token-l/', views.ProductRateViewNoTokenL.as_view()),
    path('product-rate-c/', views.ProductRateViewC.as_view()),
]

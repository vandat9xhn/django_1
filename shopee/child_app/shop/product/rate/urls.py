from django.urls import path
#
from . import views

#

urlpatterns = [
    path('product-rate-data-token-l/', views.ProductRateTokenDataView.as_view()),
    path('product-rate-data-no-token-l/', views.ProductRateNoTokenDataView.as_view()),
    path('product-rate-l/', views.ProductRateViewL.as_view()),
    path('product-rate-c/', views.ProductRateViewC.as_view()),
]

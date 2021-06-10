from django.urls import path
#
from . import views
#
from .product.urls import urlpatterns as product_urls

#

urlpatterns = [
    *product_urls,
    path('shop-l/', views.ShopViewL.as_view()),
]

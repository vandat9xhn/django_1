from django.urls import path
#
from . import views

#

urlpatterns = [
    path('cart-l/', views.CartViewL.as_view()),
    path('buy-l/', views.BuyViewL.as_view()),
    path('cancel-l/', views.CancelViewL.as_view()),
]

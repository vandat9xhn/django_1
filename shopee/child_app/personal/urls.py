from django.urls import path
#
from . import views

#

urlpatterns = [
    path('cart-lc/', views.CartViewLC.as_view()),
    path('cart-ud/', views.CartViewUD.as_view()),

    path('buy-lc/', views.BuyViewLC.as_view()),
    path('buy-d/', views.BuyViewD.as_view()),

    path('cancel-l/', views.CancelViewL.as_view()),
]

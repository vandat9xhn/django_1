from django.urls import path
#
from . import views

#

urlpatterns = [
    path('product-cmt-l/', views.ProductCmtViewL.as_view()),
    path('product-cmt-c/', views.ProductCmtViewC.as_view()),
]

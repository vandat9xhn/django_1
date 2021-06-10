from django.urls import path
#
from . import views

#

urlpatterns = [
    path('product-cmt-l/', views.ProductCmtViewL.as_view()),
]

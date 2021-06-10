from django.urls import path
#
from .views import PaymentViewL

#

urlpatterns = [
    path('payment-l/', PaymentViewL.as_view()),
]

from django.urls import path
#
from .views import VoucherViewL

#

urlpatterns = [
    path('voucher-l/', VoucherViewL.as_view()),
]

from django.urls import path
#
from .child_app.shop.urls import urlpatterns as shop_urls
from .child_app.personal.urls import urlpatterns as personal_urls
from .child_app.payment.urls import urlpatterns as payment_urls
from .child_app.transport.urls import urlpatterns as transport_urls
from .child_app.voucher.urls import urlpatterns as voucher_urls

#

urlpatterns = [
    *shop_urls,
    *personal_urls,
    *payment_urls,
    *transport_urls,
    *voucher_urls
]

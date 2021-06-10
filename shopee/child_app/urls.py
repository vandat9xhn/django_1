from .shop.urls import urlpatterns as shop_urls
from .personal.urls import urlpatterns as personal_urls
from .payment.urls import urlpatterns as payment_urls
from .transport.urls import urlpatterns as transport_urls
from .voucher.urls import urlpatterns as voucher_urls

#

urlpatterns = [
    *shop_urls,
    *personal_urls,
    *payment_urls,
    *transport_urls,
    *voucher_urls
]

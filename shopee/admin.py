from django.contrib import admin
#
from .child_app.shop.models import ShopGiftModel, ShopModel, ShopGroupModel, ShopVidPicModel, ShopVoucherPriceModel, \
    ShopVoucherAmountModel
from .child_app.shop.product.models import ProductModel, ProductVidPicModel
from .child_app.shop.product.comment.models import ProductCmtModel, ProductCmtVidPicModel
from .child_app.shop.product.rate.models import ProductRateModel
from .child_app.payment.models import PaymentModel
from .child_app.transport.models import TransportModel, TransportPriceModel
from .child_app.voucher.models import VoucherModel, VoucherPaymentModel
from .child_app.personal.models import CartModel, BuyModel, CancelModel

# Register your models here.


all_models = [
    ShopGiftModel, ShopModel, ShopGroupModel, ShopVidPicModel, ShopVoucherPriceModel, ShopVoucherAmountModel,
    ProductModel, ProductVidPicModel, ProductCmtModel, ProductCmtVidPicModel, ProductRateModel,
    PaymentModel,
    TransportModel, TransportPriceModel,
    VoucherModel, VoucherPaymentModel,
    CartModel, BuyModel, CancelModel,
]

for model in all_models:
    admin.site.register(model)

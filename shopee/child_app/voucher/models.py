from django.db import models
#
from ..payment.models import PaymentModel

# Create your models here.


class VoucherModel(models.Model):
    condition_price = models.IntegerField()
    cost = models.IntegerField()


class VoucherPaymentModel(models.Model):
    voucher_model = models.ForeignKey(VoucherModel, on_delete=models.CASCADE, related_name='vc_vc_pm')
    payment_model = models.ForeignKey(PaymentModel, on_delete=models.CASCADE, related_name='pm_vc_pm', null=True)

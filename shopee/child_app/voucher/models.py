from django.db import models
#
from ..payment.models import PaymentModel

# Create your models here.


class VoucherModel(models.Model):
    name = models.CharField(max_length=100, default='')
    cost = models.IntegerField()
    img = models.ImageField(null=True)
    info = models.TextField(default='')

    min_amount = models.IntegerField()
    expires = models.IntegerField(default=0)
    total_num = models.IntegerField(default=100)
    count_user = models.IntegerField(default=0)


class VoucherPaymentModel(models.Model):
    voucher_model = models.ForeignKey(VoucherModel, on_delete=models.CASCADE, related_name='vc_vc_pm')
    payment_model = models.ForeignKey(PaymentModel, on_delete=models.CASCADE, related_name='pm_vc_pm', null=True)

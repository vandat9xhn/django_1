from django.db import models
#
from ..shop.product.models import ProductModel
from user_profile.models import ProfileModel
#

# Create your models here.


class CartModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_cart')
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='pd_cart')
    quantity = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)


class BuyModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_buy')
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='pd_buy')

    transport_name = models.CharField(max_length=400)
    trans_price = models.IntegerField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)

    created_time = models.DateTimeField(auto_now_add=True)


class CancelModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_cc')
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='pd_cc')
    quantity = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

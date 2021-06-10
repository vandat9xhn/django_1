from django.db import models
#
from user_profile.models import ProfileModel
from ...product.models import ProductModel


# Create your models here.


class ProductRateModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_rate')
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='pd_rate')
    content = models.TextField()
    num_rate = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)

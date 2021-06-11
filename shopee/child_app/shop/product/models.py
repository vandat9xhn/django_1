from django.db import models
#
from ...shop.models import ShopModel, ShopGroupModel
#
from _common.models.valid_field import valid_vid_pic

# Create your models here.


class ProductModel(models.Model):
    shop_model = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='sh_pd')
    group_model = models.ForeignKey(ShopGroupModel, on_delete=models.CASCADE, related_name='gr_pd', null=True)

    brand = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    hashtag = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    new_price = models.IntegerField()
    old_price = models.IntegerField()
    discount = models.IntegerField()
    description = models.TextField()
    total = models.IntegerField()
    sold = models.IntegerField()

    rate = models.FloatField(default=0)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class ProductVidPicModel(models.Model):
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='pd_vp')
    vid_pic = models.FileField(validators=[valid_vid_pic], upload_to='media/shopee/product')

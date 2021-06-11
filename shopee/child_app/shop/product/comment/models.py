from django.db import models
#
from user_profile.models import ProfileModel
from ...product.models import ProductModel
#
from _common.models.valid_field import valid_vid_pic

# Create your models here.


class ProductCmtModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    product_model = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)


class ProductCmtVidPicModel(models.Model):
    comment_model = models.ForeignKey(ProductCmtModel, on_delete=models.CASCADE)
    vid_pic = models.FileField(validators=[valid_vid_pic], upload_to='media/shopee/product/cmt')

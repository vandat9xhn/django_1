from django.db import models
#
from user_profile import models as profile_models
#
from _common.models.valid_field import valid_vid_pic

# Create your models here.


class ShopModel(models.Model):
    profile_model = models.ForeignKey(profile_models.ProfileModel, on_delete=models.CASCADE, related_name='pf_sh')

    name = models.CharField(max_length=200)
    picture = models.ImageField()
    banner = models.ImageField()
    address = models.CharField(max_length=400)
    info = models.TextField()

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class ShopVidPicModel(models.Model):
    shop_model = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='sh_vp')
    vid_pic = models.FileField(validators=[valid_vid_pic])


class ShopVoucherPriceModel(models.Model):
    shop_model = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='sh_vc_pr')
    percent = models.IntegerField()
    min_price = models.IntegerField()


class ShopVoucherAmountModel(models.Model):
    shop_model = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='sh_vc_am')
    percent = models.IntegerField()
    min_amount = models.IntegerField()


class ShopGiftModel(models.Model):
    shop_model = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='sh_gift')
    image = models.ImageField()


class ShopGroupModel(models.Model):
    shop_model = models.ForeignKey(ShopModel, on_delete=models.CASCADE, related_name='sh_gr')
    group_name = models.CharField(max_length=300)

from django.db import models
#
from _common.models.valid_field import valid_vid_pic, valid_number_phone
from _common.models import choices

# Create your models here.


class PhoneLapModel(models.Model):
    name = models.CharField(max_length=200)
    type_product = models.IntegerField(choices=choices.CHOICES_TYPE_PRODUCT)
    new_price = models.IntegerField()
    old_price = models.IntegerField()

    cpu = models.TextField()
    os = models.IntegerField(choices=choices.CHOICES_OS)
    ram = models.CharField(max_length=200)
    internal_memory = models.CharField(max_length=200)
    camera = models.TextField()
    memory_stick = models.CharField(max_length=200)

    special = models.CharField(max_length=500, default='')
    cpu_type = models.IntegerField(choices=choices.CHOICES_CPU_TYPE, default=0)
    cpu_lv = models.IntegerField(choices=choices.CHOICES_CPU_LV, default=0)
    ram_lv = models.IntegerField(default=0, choices=choices.CHOICES_RAM_LV)
    internal_memory_lv = models.IntegerField(default=0, choices=choices.CHOICES_INTERNAL_MEMORY_LV)
    camera_type = models.IntegerField(default=0, choices=choices.CHOICES_CAMERA_TYPE)
    memory_stick_lv = models.IntegerField(default=0, choices=choices.CHOICES_MEMORY_STICK_LV)

    in_stock = models.IntegerField(choices=choices.CHOICES_IN_STOCK)
    discount = models.IntegerField()
    installment = models.IntegerField()

    gift = models.TextField()
    product_sets = models.TextField()
    promotion = models.TextField()


class VidPicModel(models.Model):
    phone_lap_model = models.ForeignKey(PhoneLapModel, on_delete=models.CASCADE)
    vid_pic = models.FileField(validators=[valid_vid_pic], upload_to='media/phone_lap')


class TypeModel(models.Model):
    phone_lap_model = models.ForeignKey(PhoneLapModel, on_delete=models.CASCADE)
    url = models.FileField(validators=[valid_vid_pic], upload_to='media/phone_lap')
    color = models.CharField(max_length=100)
    title = models.TextField()


class OrderModel(models.Model):
    type_model = models.ForeignKey(TypeModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number_phone = models.CharField(max_length=11, validators=[valid_number_phone])
    created_time = models.DateTimeField(auto_now_add=True)

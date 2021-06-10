from django.db import models
#
from ...models import ProfileModel
#
from _common.models import valid_field, choices
#


# Contact
class PhoneModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    phone = models.IntegerField(validators=[valid_field.valid_number_phone], null=True)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class AddressModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class MailModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    mail = models.EmailField()
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


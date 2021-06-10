from django.db import models
#
from ...models import ProfileModel
#
from _common.models import valid_field, choices
#


#  Placed
class TownModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    town = models.CharField(max_length=200)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class CityModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


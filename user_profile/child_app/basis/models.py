from django.db import models
#
from ...models import ProfileModel
#
from _common.models import valid_field, choices
#


# Basis
class GenderModel(models.Model):
    CHOICES_GENDER = [

    ]

    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class BirthModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    birth = models.DateField()
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class LanguageModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    lang = models.CharField(max_length=50)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)



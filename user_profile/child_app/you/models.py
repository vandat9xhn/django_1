from django.db import models
#
from ...models import ProfileModel
#
from _common.models import valid_field, choices
#


# You
class AboutYouModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    you = models.TextField()
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class HobbyModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    hobby = models.TextField()
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class OtherNameModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    other_name = models.CharField(max_length=200)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


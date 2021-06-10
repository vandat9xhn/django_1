from django.db import models
#
from ...models import ProfileModel
#
from _common.models import valid_field, choices
#


# Work
class WorkModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    work = models.CharField(max_length=200)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class UniversityModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    university = models.CharField(max_length=200)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)


class SchoolModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)



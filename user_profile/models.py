from django.db import models
#
from _common.models import valid_field, choices


# Create your models here.


class ProfileModel(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    is_online = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)


class NameModel(models.Model):
    profile_model = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    updated_time = models.DateTimeField(auto_now=True)


class PersonalSettingModel(models.Model):
    profile_model = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, primary_key=True)
    permission_see_friend = models.IntegerField(default=0)
    permission_add_friend = models.IntegerField(default=0)
    permission_follow = models.IntegerField(default=0)
    permission_post = models.IntegerField(default=0)

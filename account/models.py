from django.db import models
#
from user_profile.models import ProfileModel

# Create your models here.


class RefreshTokenModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_rf_t')
    refresh_token = models.CharField(max_length=300)
    updated_time = models.DateTimeField(auto_now=True)

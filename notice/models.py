from django.db import models
#
from user_profile.models import ProfileModel
#
from _common.models.choices import CHOICES_STATUS_SEEN

# Create your models here.


class NoticeModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='nt_pf')
    friend_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='nt_fr')

    link_id = models.CharField(max_length=200)
    content = models.TextField()
    status_seen = models.IntegerField(choices=CHOICES_STATUS_SEEN)
    updated_time = models.DateTimeField(auto_now=True)

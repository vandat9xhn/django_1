from django.db import models
#
from ...post.models import PostModel

from user_profile.models import ProfileModel
#
from _common.models.choices import CHOICES_LIKE


# Create your models here.


class LikeModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_like', null=True)
    post_model = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='p_like')
    type_like = models.IntegerField(choices=CHOICES_LIKE)


class ShareModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_share', null=True)
    post_model = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='p_share')
    count = models.IntegerField()

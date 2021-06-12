from django.db import models
#
from user_profile.models import ProfileModel
#
from facebook.child_app.post.models import PostModel
#
from _common.models import choices


# Create your models here.


# picture
class PictureModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    url = models.CharField(max_length=300, null=True)
    post_model = models.OneToOneField(PostModel, on_delete=models.CASCADE, related_name='p_pic')
    # permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)
    is_active = models.BooleanField(default=True)


# cover
class CoverModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    url = models.CharField(max_length=300, null=True)
    # post_id = models.IntegerField(null=True)
    # permission = models.IntegerField(choices=choices.CHOICES_PERMISSION_USER, default=0)
    post_model = models.OneToOneField(PostModel, on_delete=models.CASCADE, related_name='p_cover')
    is_active = models.BooleanField(default=True)

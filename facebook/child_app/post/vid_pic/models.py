from django.db import models
#
from user_profile.models import ProfileModel

from ...post.models import PostModel
#
from _common.models import valid_field, choices, clean_field


# Create your models here.


class VidPicModel(models.Model):
    post_model = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='p_v_p')
    content = models.TextField(null=True, default='')
    vid_pic = models.FileField(validators=[valid_field.valid_vid_pic], null=True)

    def clean(self):
        clean_field.clean_content_vid_pic(self.content, self.vid_pic)


#
class VidPicLikeModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_vp_l')
    vid_pic_model = models.ForeignKey(VidPicModel, on_delete=models.CASCADE, related_name='vp_like')
    type_like = models.IntegerField(choices=choices.CHOICES_LIKE)


class VidPicShareModel(models.Model):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_vp_sh')
    vid_pic_model = models.ForeignKey(VidPicModel, on_delete=models.CASCADE, related_name='vp_share')
    count = models.IntegerField()


#
class VidPicHistoryModel(models.Model):
    vid_pic_model = models.ForeignKey(VidPicModel, on_delete=models.CASCADE, related_name='vp_his')
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

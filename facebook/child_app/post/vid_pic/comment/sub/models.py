from django.db import models
#
from user_profile.models import ProfileModel

from ...comment.models import VidPicCmtModel
#
from _common.models import cmt_sub_abstract


# Create your models here.


class VidPicSubModel(cmt_sub_abstract.CommentSubModel):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_vp_sub')
    comment_model = models.ForeignKey(VidPicCmtModel, on_delete=models.CASCADE, related_name='cmt_sub')


class VidPicSubLikeModel(cmt_sub_abstract.LikeModel):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_vp_sub_like')
    sub_model = models.ForeignKey(VidPicSubModel, on_delete=models.CASCADE, related_name='sub_like')


class VidPicSubHistoryModel(cmt_sub_abstract.HistoryModel):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_vp_sub_his')
    sub_model = models.ForeignKey(VidPicSubModel, on_delete=models.CASCADE, related_name='sub_his')

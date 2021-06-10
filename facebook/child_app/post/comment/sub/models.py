from django.db import models
#
from user_profile.models import ProfileModel

from ...comment.models import CommentModel
#
from _common.models import cmt_sub_abstract


# Create your models here.


class SubModel(cmt_sub_abstract.CommentSubModel):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_sub')
    comment_model = models.ForeignKey(CommentModel, on_delete=models.CASCADE, related_name='cmt_sub')


class SubLikeModel(cmt_sub_abstract.LikeModel):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_sub_l')
    sub_model = models.ForeignKey(SubModel, on_delete=models.CASCADE, related_name='sub_like')


class SubHistoryModel(cmt_sub_abstract.HistoryModel):
    sub_model = models.ForeignKey(SubModel, on_delete=models.CASCADE, related_name='sub_his')

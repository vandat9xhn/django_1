from django.db import models
#
from user_profile.models import ProfileModel

from ...post.models import PostModel
#
from _common.models import cmt_sub_abstract


# Create your models here.


class CommentModel(cmt_sub_abstract.CommentSubModel):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_cmt')
    post_model = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='p_cmt')


class CmtLikeModel(cmt_sub_abstract.LikeModel):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_cmt_l')
    comment_model = models.ForeignKey(CommentModel, on_delete=models.CASCADE, related_name='cmt_cmt_like')


class CmtHistoryModel(cmt_sub_abstract.HistoryModel):
    comment_model = models.ForeignKey(CommentModel, on_delete=models.CASCADE, related_name='cmt_cmt_his')

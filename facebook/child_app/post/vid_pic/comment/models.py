from django.db import models
#
from user_profile.models import ProfileModel

from ...vid_pic.models import VidPicModel
#
from _common.models import cmt_sub_abstract


# Create your models here.


class VidPicCmtModel(cmt_sub_abstract.CommentSubModel):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_vp_cmt')
    vid_pic_model = models.ForeignKey(VidPicModel, on_delete=models.CASCADE, related_name='vp_vp_vmt')


class VidPicCmtLikeModel(cmt_sub_abstract.LikeModel):
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='pf_vp_cmt_l')
    vid_pic_Cmt_model = models.ForeignKey(VidPicCmtModel, on_delete=models.CASCADE, related_name='vp_cmt_like')


class VidPicCmtHistoryModel(cmt_sub_abstract.HistoryModel):
    vid_pic_Cmt_model = models.ForeignKey(VidPicCmtModel, on_delete=models.CASCADE, related_name='vp_cmt_his')

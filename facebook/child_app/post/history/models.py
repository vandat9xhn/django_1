from django.db import models
#
from ...post.models import PostModel

#


class HistoryModel(models.Model):
    post_model = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='p_his')
    content = models.TextField(null=True, default='')
    created_time = models.DateTimeField(auto_now_add=True)


class HistoryVidPicCreateModel(models.Model):
    his_model = models.ForeignKey(HistoryModel, on_delete=models.CASCADE, related_name='h_h_v_p_c')
    vid_pic = models.TextField()


class HistoryVidPicDelModel(models.Model):
    his_model = models.ForeignKey(HistoryModel, on_delete=models.CASCADE, related_name='h_h_v_p_d')
    vid_pic = models.TextField()

from django.db import models
#
from _common.models import valid_field, choices, clean_field


# Create your models here.


class CommentSubModel(models.Model):
    content = models.TextField(null=True)
    vid_pic = models.FileField(validators=[valid_field.valid_vid_pic], null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def clean(self):
        clean_field.clean_content_vid_pic(self.content, self.vid_pic)


class LikeModel(models.Model):
    type_like = models.IntegerField(choices=choices.CHOICES_LIKE)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class HistoryModel(models.Model):
    content = models.TextField(null=True)
    vid_pic = models.TextField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def clean(self):
        clean_field.clean_content_vid_pic(self.content, self.vid_pic)

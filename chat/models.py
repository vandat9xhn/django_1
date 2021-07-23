from django.db import models
#
from user_profile.models import ProfileModel
#
from _common.models.valid_field import valid_vid_pic
from _common.models.choices import CHOICES_LIKE

# Create your models here.


class RoomModel(models.Model):
    room_chat = models.CharField(max_length=100, unique=True, primary_key=True)
    is_group = models.BooleanField()
    owner = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='r_o')
    creator = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='r_cr')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class RoomUserModel(models.Model):
    room_model = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)

    is_notice = models.BooleanField(default=True)
    on_chat = models.BooleanField(default=False)
    on_input = models.BooleanField(default=False)

    begin_mess = models.IntegerField(default=0)
    last_mess = models.IntegerField(default=0)
    last_receive = models.IntegerField(default=0)
    last_seen = models.IntegerField(default=0)

    joined_time = models.DateTimeField(auto_now_add=True)


class MessageModel(models.Model):
    room_model = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    message = models.TextField()
    created_time = models.DateTimeField(auto_now=True)


class VidPicModel(models.Model):
    mess_model = models.ForeignKey(MessageModel, on_delete=models.CASCADE)
    vid_pic = models.FileField(validators=[valid_vid_pic], upload_to='media/chat')


class LikeModel(models.Model):
    mess_model = models.ForeignKey(MessageModel, on_delete=models.CASCADE)
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE)
    type_like = models.IntegerField(choices=CHOICES_LIKE)
    created_time = models.DateTimeField(auto_now=True)


# group


class TimelineModel(models.Model):
    room_model = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='tl_pf')
    friend_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='tl_fr')
    status = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now=True)

from django.db import models
from django.db.models import Q
from django.conf import settings
#
from user_profile.models import ProfileModel


# Create your models here.


class FriendModel(models.Model):
    requester = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='fr_rq')
    receiver = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='fr_rc')
    created_time = models.DateField(auto_now_add=True)


class AddFriendModel(models.Model):
    requester = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='a_fr_rq')
    receiver = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='a_fr_rc')
    created_time = models.DateField(auto_now_add=True)


# ------------- 0: having no mutual friend
# ------------- 1: having at least 1 mutual friend
# ------------- 2: user's friend
# ------------- 3: current user


def get_user_id(user):
    if type(user) == int or type(user) == str:
        user_id = user
    elif not user and settings.DEBUG:
        user_id = 0
    else:
        user_id = user.id

    return user_id


def get_friend_id_arr(user):
    user_id = get_user_id(user)

    return [
        *FriendModel.objects.filter(requester=user_id).values_list('receiver', flat=True),
        *FriendModel.objects.filter(receiver=user_id).values_list('requester', flat=True)
    ]


def count_friend_mutual(user_1, user_2):
    friend_arr_user_1 = get_friend_id_arr(user_1)
    friend_arr_user_2 = get_friend_id_arr(user_2)

    return len(set(friend_arr_user_1).intersection(set(friend_arr_user_2)))


def friend_relative_num(user, friend):
    user_id = get_user_id(user)
    friend_id = get_user_id(friend)

    relative = 0

    if str(user_id) == str(friend_id):
        relative = 3
    elif FriendModel.objects.filter(
            Q(requester=user_id, receiver=friend_id) | Q(requester=friend_id, receiver=user_id)):
        relative = 2
    elif count_friend_mutual(user_id, friend_id) > 0:
        relative = 1

    return relative


def friend_has_permission(user, friend, permission):
    relative = friend_relative_num(user, friend)

    if relative < permission:
        return False

    return True

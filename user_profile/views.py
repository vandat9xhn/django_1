from django.db.models import Q
#
from rest_framework.generics import RetrieveAPIView
#
from _common.views.user_update import UserUpdateOnlyOne
#
from . import serializers, models


# Create your views here.


# ------------- COMMON -----------


class ProfileView:
    queryset = models.ProfileModel.objects.all()
    serializer_class = serializers.ProfileSerializer


class NameView:
    queryset = models.NameModel.objects.all()
    serializer_class = serializers.NameSerializer


class PersonalSettingView:
    queryset = models.PersonalSettingModel.objects.all()
    serializer_class = serializers.PersonalSettingSerializer


# ------------------------


#
# class ProfileViewL(ProfileView, ListAPIView):
#     pass


class ProfileViewR(ProfileView, RetrieveAPIView):
    pass


#
class NameViewU(NameView, UserUpdateOnlyOne):
    pass


class PersonalSettingViewU(PersonalSettingView, UserUpdateOnlyOne):
    pass

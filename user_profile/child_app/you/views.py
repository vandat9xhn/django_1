#
from . import models
from . import serializers
#
from _common.views.user_update import UserUpdateView, UserUpdateOnlyOne
from _common.views.user_create import UserCreateView
from _common.views.user_delete import UserDestroyView


#


# ------------------------


class AboutYouView:
    serializer_class = serializers.AboutYouSerializer
    queryset = models.AboutYouModel.objects.all()


class HobbyView:
    serializer_class = serializers.HobbySerializer
    queryset = models.HobbyModel.objects.all()


class OtherNameView:
    serializer_class = serializers.OtherNameSerializer
    queryset = models.OtherNameModel.objects.all()


# -------------------------


#
class AboutYouViewU(AboutYouView, UserUpdateOnlyOne):
    pass


#
class HobbyViewU(HobbyView, UserUpdateOnlyOne):
    pass


#
class OtherNameViewC(OtherNameView, UserCreateView):
    pass


class OtherNameViewUD(OtherNameView, UserUpdateView, UserDestroyView):
    pass

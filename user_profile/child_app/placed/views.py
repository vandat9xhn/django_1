#
from . import models
from . import serializers
#
from _common.views.user_update import UserUpdateView
from _common.views.user_create import UserCreateView
from _common.views.user_delete import UserDestroyView


#


# ------------------------


class TownView:
    serializer_class = serializers.TownSerializer
    queryset = models.TownModel


class CityView:
    serializer_class = serializers.CitySerializer
    queryset = models.CityModel


# -------------------------


#
class TownViewC(TownView, UserCreateView):
    pass


class TownViewUD(TownView, UserUpdateView, UserDestroyView):
    pass


#
class CityViewC(CityView, UserCreateView):
    pass


class CityViewUD(CityView, UserUpdateView, UserDestroyView):
    pass

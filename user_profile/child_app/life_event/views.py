#
from . import models
from . import serializers
#
from _common.views.user_update import UserUpdateView
from _common.views.user_create import UserCreateView
from _common.views.user_delete import UserDestroyView


#


# ------------------------


class LifeEventView:
    serializer_class = serializers.LifeEventSerializer
    queryset = models.LifeEventModel


# -------------------------


class LifeEventViewC(LifeEventView, UserCreateView):
    pass


class LifeEventViewUD(LifeEventView, UserUpdateView, UserDestroyView):
    pass

#
from . import models
from . import serializers
#
from _common.views.user_update import UserUpdateView, UserUpdateOnlyOne
from _common.views.user_create import UserCreateView
from _common.views.user_delete import UserDestroyView


#


# ------------------------


class RelationView:
    serializer_class = serializers.RelationSerializer
    queryset = models.RelationModel.objects.all()


class FamilyView:
    serializer_class = serializers.FamilySerializer
    queryset = models.FamilyModel.objects.all()


# -------------------------


#
class RelationViewU(RelationView, UserUpdateOnlyOne):
    pass


#
class FamilyViewC(FamilyView, UserCreateView):
    pass


class FamilyViewUD(FamilyView, UserUpdateView, UserDestroyView):
    pass

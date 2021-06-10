#
from . import models
from . import serializers
#
from _common.views.user_update import UserUpdateOnlyOne


#


# ------------------------


class GenderView:
    serializer_class = serializers.GenderSerializer
    queryset = models.GenderModel


class BirthView:
    serializer_class = serializers.BirthSerializer
    queryset = models.BirthModel


class LanguageView:
    serializer_class = serializers.LanguageSerializer
    queryset = models.LanguageModel


# -------------------------


class GenderViewU(GenderView, UserUpdateOnlyOne):
    pass


class BirthViewU(BirthView, UserUpdateOnlyOne):
    pass


class LanguageViewU(LanguageView, UserUpdateOnlyOne):
    pass

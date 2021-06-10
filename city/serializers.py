
#
from . import models
#
from _common.serializers.custom_field import FieldSerializer
#


class HistorySerializer(FieldSerializer):
    name_field = 'history[]'
    #

    class Meta:
        model = models.HistoryModel
        fields = '__all__'


class CitySerializer(FieldSerializer):
    name_field = 'city[]'
    #

    class Meta:
        model = models.CityModel
        fields = '__all__'

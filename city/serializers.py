
#
from . import models
#
from _common.serializers.custom_field import FieldSerializer
from _common.serializers.data_user import DataProfileSerializer
#


class HistorySerializer(FieldSerializer):
    name_field = 'history'
    #

    class Meta:
        model = models.HistoryModel
        fields = '__all__'


class CitySerializer(DataProfileSerializer):
    name_field = 'city'
    #

    class Meta:
        model = models.CityModel
        fields = '__all__'

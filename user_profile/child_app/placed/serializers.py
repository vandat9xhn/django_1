from rest_framework.serializers import ModelSerializer
#
from . import models
#
from _common.serializers import custom_field

#


class CitySerializer(custom_field.FieldSerializer):
    name_field = 'city[]'

    class Meta:
        model = models.CityModel
        fields = '__all__'


class TownSerializer(custom_field.FieldSerializer):
    name_field = 'town[]'

    class Meta:
        model = models.TownModel
        fields = '__all__'

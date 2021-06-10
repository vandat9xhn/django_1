from rest_framework.serializers import ModelSerializer
#
from . import models
#
from _common.serializers import custom_field

#


class LifeEventSerializer(custom_field.FieldSerializer):
    name_field = 'life_event[]'

    class Meta:
        model = models.LifeEventModel
        fields = '__all__'

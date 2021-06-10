from rest_framework.serializers import ModelSerializer
#
from . import models
#
from _common.serializers import custom_field

#


class FamilySerializer(custom_field.FieldSerializer):
    name_field = 'family[]'

    class Meta:
        model = models.FamilyModel
        fields = '__all__'


class RelationSerializer(custom_field.FieldSerializer):
    name_field = 'relation[]'

    class Meta:
        model = models.RelationModel
        fields = '__all__'

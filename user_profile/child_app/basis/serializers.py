from rest_framework.serializers import ModelSerializer
#
from . import models
#
from _common.serializers import custom_field

#


class GenderSerializer(custom_field.FieldSerializer):
    name_field = 'genders'

    class Meta:
        model = models.GenderModel
        fields = '__all__'


class BirthSerializer(custom_field.FieldSerializer):
    name_field = 'births'

    class Meta:
        model = models.BirthModel
        fields = '__all__'


class LanguageSerializer(custom_field.FieldSerializer):
    name_field = 'langs'

    class Meta:
        model = models.LanguageModel
        fields = '__all__'

from rest_framework.serializers import ModelSerializer
#
from . import models
#
from _common.serializers import custom_field

#


class WorkSerializer(custom_field.FieldSerializer):
    name_field = 'work[]'

    class Meta:
        model = models.WorkModel
        fields = '__all__'


class SchoolSerializer(custom_field.FieldSerializer):
    name_field = 'school[]'

    class Meta:
        model = models.SchoolModel
        fields = '__all__'


class UniversitySerializer(custom_field.FieldSerializer):
    name_field = 'university[]'

    class Meta:
        model = models.UniversityModel
        fields = '__all__'

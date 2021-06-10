from rest_framework.serializers import ModelSerializer
#
from . import models
#
from _common.serializers import custom_field

#


class MailSerializer(custom_field.FieldSerializer):
    name_field = 'mail[]'

    class Meta:
        model = models.MailModel
        fields = '__all__'


class PhoneSerializer(custom_field.FieldSerializer):
    name_field = 'phone[]'

    class Meta:
        model = models.PhoneModel
        fields = '__all__'


class AddressSerializer(custom_field.FieldSerializer):
    name_field = 'address[]'

    class Meta:
        model = models.AddressModel
        fields = '__all__'

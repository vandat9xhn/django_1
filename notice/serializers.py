from rest_framework.serializers import SerializerMethodField
#
from . import models
#
from _common.serializers.data_user import DataProfileSerializer

#


class NoticeSerializer(DataProfileSerializer):
    name_field = 'notice'

    class Meta:
        model = models.NoticeModel
        fields = '__all__'

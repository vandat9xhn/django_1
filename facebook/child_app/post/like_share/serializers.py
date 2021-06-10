# from rest_framework.serializers import SerializerMethodField
#
from .models import LikeModel, ShareModel
#
from _common.serializers.data_field import FieldSerializer


#


class LikeSerializer(FieldSerializer):

    class Meta:
        model = LikeModel
        fields = '__all__'


class ShareSerializer(FieldSerializer):
    class Meta:
        model = ShareModel
        fields = '__all__'

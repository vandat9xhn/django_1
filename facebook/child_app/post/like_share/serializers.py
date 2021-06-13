from .models import LikeModel, ShareModel
#
from _common.serializers.facebook.post import InteractiveSerializer


#


class LikeSerializer(InteractiveSerializer):
    class Meta:
        model = LikeModel
        fields = '__all__'


class ShareSerializer(InteractiveSerializer):
    class Meta:
        model = ShareModel
        fields = '__all__'

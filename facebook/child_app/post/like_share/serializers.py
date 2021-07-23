from .models import LikeModel, ShareModel
#
from _common.serializers.facebook.post import InteractiveSerializer


#


class LikeSerializer(InteractiveSerializer):
    name_field = 'likes'

    class Meta:
        model = LikeModel
        fields = '__all__'


class ShareSerializer(InteractiveSerializer):
    name_field = 'shares'

    class Meta:
        model = ShareModel
        fields = '__all__'

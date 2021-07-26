from .models import LikeModel, ShareModel
#
from _common.serializers.facebook.post import InteractiveSerializer


#


class LikeSerializer(InteractiveSerializer):
    name_field = 'like'

    class Meta:
        model = LikeModel
        fields = '__all__'


class ShareSerializer(InteractiveSerializer):
    name_field = 'share'

    class Meta:
        model = ShareModel
        fields = '__all__'

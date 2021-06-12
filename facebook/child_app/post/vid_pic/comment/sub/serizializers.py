from rest_framework.serializers import SerializerMethodField
#
from .models import VidPicSubModel, VidPicSubLikeModel, VidPicSubHistoryModel
#
from _common.serializers.data_field import FieldSerializer, DataLikeSerializer


#


#


class VidPicSubLikeSerializer(FieldSerializer):
    name_field = 'vid_pic_sub_like[]'

    #

    class Meta:
        fields = '__all__'
        model = VidPicSubLikeModel


class VidPicSubHistorySerializer(FieldSerializer):
    name_field = 'vid_pic_sub_history[]'

    #

    class Meta:
        fields = '__all__'
        model = VidPicSubHistoryModel


class VidPicSubSerializer(DataLikeSerializer):
    name_field = 'vid_pic_sub[]'
    #
    like_obj = SerializerMethodField('get_like_obj')
    history_obj = SerializerMethodField('get_history_obj')

    class Meta:
        fields = '__all__'
        model = VidPicSubModel

    def get_like_obj(self, instance):
        return self.get_data_like(
            VidPicSubLikeSerializer,
            VidPicSubLikeModel.objects.filter(sub_model=instance.id),
            'vid_pic_sub_like',
        )

    def get_history_obj(self, instance):
        return self.get_arr_count(
            VidPicSubHistorySerializer,
            VidPicSubHistoryModel.objects.filter(sub_model=instance.id),
            'vid_pic_sub_his',
        )

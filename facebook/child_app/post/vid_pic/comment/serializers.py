from rest_framework.serializers import SerializerMethodField
#
from .models import VidPicCmtModel, VidPicCmtLikeModel, VidPicCmtHistoryModel
#
from _common.serializers.data_field import FieldSerializer, DataLikeSerializer


#


#


class VidPicCmtLikeSerializer(FieldSerializer):
    name_field = 'vid_pic_cmt_likes[]'

    #

    class Meta:
        fields = '__all__'
        model = VidPicCmtLikeModel


class VidPicCmtHistorySerializer(FieldSerializer):
    name_field = 'vid_pic_cmt_histories[]'
    #

    class Meta:
        fields = '__all__'
        model = VidPicCmtHistoryModel


class VidPicCmtSerializer(DataLikeSerializer):
    name_field = 'vid_pic_cmts[]'
    #
    like_obj = SerializerMethodField('get_like_obj')
    history_obj = SerializerMethodField('get_history_obj')

    class Meta:
        fields = '__all__'
        model = VidPicCmtModel

    def get_like_obj(self, instance):
        return self.get_data_like(
            VidPicCmtLikeSerializer,
            VidPicCmtLikeModel.objects.filter(Cmt_model=instance.id),
            'vid_pic_cmt_like',
        )

    def get_history_obj(self, instance):
        return self.get_arr_count(
            VidPicCmtHistorySerializer,
            VidPicCmtHistoryModel.objects.filter(Cmt_model=instance.id),
            'vid_pic_cmt_his',
        )

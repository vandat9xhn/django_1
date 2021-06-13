from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import DataLikeShareSerializer, FieldSerializer
#
from .models import VidPicModel, VidPicLikeModel, VidPicShareModel, VidPicHistoryModel

from .comment.serializers import VidPicCmtSerializer, VidPicCmtModel

#


class VidPicLikeSerializer(FieldSerializer):
    name_field = 'vid_pic_like[]'
    #

    class Meta:
        model = VidPicLikeModel
        fields = '__all__'


class VidPicShareSerializer(FieldSerializer):
    name_field = 'vid_pic_share[]'
    #

    class Meta:
        model = VidPicShareModel
        fields = '__all__'


class VidPicHistorySerializer(FieldSerializer):
    name_field = 'vid_pic_history[]'
    #

    class Meta:
        model = VidPicHistoryModel
        fields = '__all__'


#


class VidPicSerializer(DataLikeShareSerializer):
    name_field = 'vid_pic[]'
    #
    comment_obj = SerializerMethodField('get_comment_obj')
    like_obj = SerializerMethodField('get_like_obj')
    share_obj = SerializerMethodField('get_share_obj')
    his_obj = SerializerMethodField('get_his_obj')

    class Meta:
        model = VidPicModel
        fields = '__all__'

    def get_comment_obj(self, instance):

        return self.get_arr_count(
            VidPicCmtSerializer,
            VidPicCmtModel.objects.filter(vid_pic_model=instance.id),
            'vid_pic_cmt',
        )

    def get_like_obj(self, instance):

        return self.get_data_like(
            VidPicLikeSerializer,
            VidPicLikeModel.objects.filter(vid_pic_model=instance.id),
            'vid_pic_like',
        )

    def get_share_obj(self, instance):

        return self.get_data_share(
            VidPicShareSerializer,
            VidPicShareModel.objects.filter(vid_pic_model=instance.id),
            'vid_pic_share',
        )

    def get_his_obj(self, instance):

        return self.get_arr_count(
            VidPicHistorySerializer,
            VidPicHistoryModel.objects.filter(vid_pic_model=instance.id),
            'vid_pic_his',
        )

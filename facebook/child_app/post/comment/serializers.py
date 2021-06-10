from rest_framework.serializers import SerializerMethodField
#
from .models import CommentModel, CmtLikeModel, CmtHistoryModel
#
from _common.serializers.data_field import FieldSerializer, DataLikeSerializer
#


#


class CmtLikeSerializer(FieldSerializer):
    name_field = 'cmt_likes[]'
    #

    class Meta:
        fields = '__all__'
        model = CmtLikeModel


class CmtHistorySerializer(FieldSerializer):
    name_field = 'cmt_histories[]'
    #

    class Meta:
        fields = '__all__'
        model = CmtHistoryModel


class CommentSerializer(DataLikeSerializer):
    name_field = 'comments[]'
    #
    like_obj = SerializerMethodField('get_like_obj')
    history_obj = SerializerMethodField('get_history_obj')

    class Meta:
        fields = '__all__'
        model = CommentModel

    def get_like_obj(self, instance):
        return self.get_data_like(
            CmtLikeSerializer,
            CmtLikeModel.objects.filter(comment_model=instance.id),
            'cmt_like',
        )

    def get_history_obj(self, instance):
        return self.get_arr_count(
            CmtHistorySerializer,
            CmtHistoryModel.objects.filter(comment_model=instance.id),
            'cmt_his',
        )

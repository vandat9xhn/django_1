from rest_framework.serializers import SerializerMethodField
#
from .models import CommentModel, CmtLikeModel, CmtHistoryModel
#
from .sub.serizializers import SubSerializer, SubModel
#
from _common.serializers.data_field import FieldSerializer, DataLikeSerializer
#


#


class CmtLikeSerializer(FieldSerializer):
    name_field = 'cmt_likes'
    #

    class Meta:
        fields = '__all__'
        model = CmtLikeModel


class CmtHistorySerializer(FieldSerializer):
    name_field = 'cmt_historys'
    #

    class Meta:
        fields = '__all__'
        model = CmtHistoryModel


class CommentSerializer(DataLikeSerializer):
    name_field = 'comments'
    #
    sub_obj = SerializerMethodField()
    like_obj = SerializerMethodField()
    history_obj = SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = CommentModel

    def get_sub_obj(self, instance):
        return self.get_arr_count(
            SubSerializer,
            SubModel.objects.filter(comment_model=instance.id),
            'cmt_sub',
        )

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

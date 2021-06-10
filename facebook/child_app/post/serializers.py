from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import DataLikeShareSerializer
#
from .models import PostModel

from .comment.serializers import CommentModel, CommentSerializer
from .vid_pic.serializers import VidPicModel, VidPicSerializer
from .history.serializers import HistorySerializer, HistoryModel
from .like_share.serializers import LikeSerializer, LikeModel, ShareSerializer, ShareModel


#


class PostSerializer(DataLikeShareSerializer):
    name_field = 'posts[]'
    #
    comment_obj = SerializerMethodField('get_comment_obj')
    vid_pic_obj = SerializerMethodField('get_vid_pic_obj')
    like_obj = SerializerMethodField('get_like_obj')
    share_obj = SerializerMethodField('get_share_obj')
    his_obj = SerializerMethodField('get_his_obj')

    class Meta:
        model = PostModel
        fields = '__all__'

    def get_comment_obj(self, instance):

        return self.get_arr_count(
            CommentSerializer,
            CommentModel.objects.filter(post_model=instance.id),
            'comment',
        )

    def get_vid_pic_obj(self, instance):
        return self.get_arr_count(
            VidPicSerializer,
            VidPicModel.objects.filter(post_model=instance.id),
            'vid_pic',
        )

    def get_like_obj(self, instance):
        return self.get_data_like(
            LikeSerializer,
            LikeModel.objects.filter(post_model=instance.id),
            'like'
        )

    def get_share_obj(self, instance):
        return self.get_data_share(
            ShareSerializer,
            ShareModel.objects.filter(post_model=instance.id),
            'share'
        )

    def get_his_obj(self, instance):
        return self.get_arr_count(
            HistorySerializer,
            HistoryModel.objects.filter(post_model=instance.id),
            'his'
        )

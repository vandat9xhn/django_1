from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import DataLikeShareSerializer
from _common.serializers.content_field import ContentFieldSerializer
#
from .models import PostModel
#
from .comment.serializers import CommentModel, CommentSerializer
from .vid_pic.serializers import VidPicModel, VidPicSerializer
from .history.serializers import HistorySerializer, HistoryModel
from .like_share.serializers import LikeSerializer, LikeModel, ShareSerializer, ShareModel


#
class PostSerializer(DataLikeShareSerializer, ContentFieldSerializer):
    name_field = 'post'
    #
    content_obj = SerializerMethodField()
    comment_obj = SerializerMethodField()
    vid_pic_obj = SerializerMethodField()
    like_obj = SerializerMethodField()
    share_obj = SerializerMethodField()
    his_obj = SerializerMethodField()

    class Meta:
        model = PostModel
        fields = '__all__'

    def get_content_obj(self, instance):
        return self.get_content_more(instance.content)

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

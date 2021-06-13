from rest_framework.generics import ListAPIView, RetrieveAPIView
#
from . import models, serializers
#
from _common.views.facebook.post import FollowPostViewL, FollowVidPicViewL
from _common.views.user_create import UserCreateLike, UserCreateShare
from _common.views.user_update import UserUpdateToHistoryView
from _common.views.user_delete import UserDestroyView
from _common.views.permission_view import PermissionViewR


# --------------


class VidPicView:
    queryset = models.VidPicModel.objects.all()
    serializer_class = serializers.VidPicSerializer


class VidPicLikeView:
    queryset = models.VidPicLikeModel.objects.all()
    serializer_class = serializers.VidPicLikeSerializer


class VidPicShareView:
    queryset = models.VidPicShareModel.objects.all()
    serializer_class = serializers.VidPicShareSerializer


class VidPicHistoryView:
    queryset = models.VidPicHistoryModel.objects.all()
    serializer_class = serializers.VidPicHistorySerializer


# --------------


#
class VidPicViewL(VidPicView, FollowPostViewL):
    pass


class VidPicTypePostViewL(VidPicView, ListAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        type_post = self.request.query_params.get('type_post')

        return self.queryset.filter(post_model__type_post=type_post, post_model__profile_model=user_id)


class VidPicViewRUD(VidPicView, RetrieveAPIView, UserUpdateToHistoryView, UserDestroyView):

    @staticmethod
    def get_update_fields():
        return ['content']

    def handle_model_history(self, instance, data_history):
        models.VidPicHistoryModel.objects.create(
            vid_pic_model=instance,
            **data_history,
        )


#
class VidPicLikeViewLC(VidPicLikeView, FollowVidPicViewL, UserCreateLike):
    pass


#
class VidPicShareViewLC(VidPicShareView, FollowVidPicViewL, UserCreateShare):

    @staticmethod
    def get_max_share():
        return 5

    def get_count_user_share(self):
        user_id = self.request.user.id
        vid_pic_id = self.request.data.get('vid_pic_model')

        return self.queryset.get(profile_model=user_id, vid_pic_model=vid_pic_id).count


#
class VidPicHistoryViewL(VidPicHistoryView, FollowVidPicViewL):
    pass

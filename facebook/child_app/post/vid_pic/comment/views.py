from rest_framework.generics import ListAPIView
#
from . import models, serializers
#
from _common.views.user_create import UserCreateView, UserCreateLike
from _common.views.user_update import UserUpdateToHistoryView
from _common.views.user_delete import UserDestroyView
from _common.views.facebook.post import FollowVidPicViewL, FollowVidPicCmtViewL


# Create your views here.


# ----------------


class VidPicCmtView:
    queryset = models.VidPicCmtModel.objects.all()
    serializer_class = serializers.VidPicCmtSerializer


class VidPicCmtLikeView:
    queryset = models.VidPicCmtLikeModel.objects.all()
    serializer_class = serializers.VidPicCmtLikeSerializer


class VidPicCmtHistoryView:
    queryset = models.VidPicCmtHistoryModel.objects.all()
    serializer_class = serializers.VidPicCmtHistorySerializer


# -------------


class VidPicCmtLikeHistoryViewL(FollowVidPicCmtViewL):

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter more permission here
        return queryset


# ----------------


class VidPicCmtViewLC(VidPicCmtView, FollowVidPicViewL, UserCreateView):

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter more permission here
        return queryset


class VidPicCmtViewUD(VidPicCmtView, UserUpdateToHistoryView, UserDestroyView):

    @staticmethod
    def get_update_fields():
        return ['content', 'vid_pic']

    def handle_model_history(self, instance, data_history):
        models.VidPicCmtHistoryModel.objects.create(
            comment_model=instance,
            **data_history,
        )


#
class VidPicCmtLikeViewLC(VidPicCmtLikeView, VidPicCmtLikeHistoryViewL, UserCreateLike):

    def get_instance_create(self):
        comment_id = self.request.data.get('vid_pic_comment_model')

        return self.queryset.get(comment_model=comment_id, profile_model=self.request.user.id)


#
class VidPicCmtHistoryViewL(VidPicCmtHistoryView, VidPicCmtLikeHistoryViewL):
    pass

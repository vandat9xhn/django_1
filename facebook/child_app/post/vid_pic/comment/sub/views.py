#
from . import models, serizializers
#
from _common.views.user_create import UserCreateView, UserCreateLike
from _common.views.user_update import UserUpdateToHistoryView
from _common.views.user_delete import UserDestroyView
from _common.views.facebook.post import FollowVidPicCmtViewL, FollowVidPicSubViewL, get_like_queryset


# Create your views here.


# -------------


class VidPicSubView:
    queryset = models.VidPicSubModel.objects.all()
    serializer_class = serizializers.VidPicSubSerializer


class VidPicSubLikeView:
    queryset = models.VidPicSubLikeModel.objects.all()
    serializer_class = serizializers.VidPicSubLikeSerializer


class VidPicSubHistoryView:
    queryset = models.VidPicSubHistoryModel.objects.all()
    serializer_class = serizializers.VidPicSubHistorySerializer


# -------------


class VidPicSubLikeHistoryViewL(FollowVidPicSubViewL):

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter more permission

        return queryset


# -------------


#
class VidPicSubViewLC(VidPicSubView, FollowVidPicCmtViewL, UserCreateView):

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter more permission

        return queryset


class VidPicSubViewUD(VidPicSubView, UserUpdateToHistoryView, UserDestroyView):

    def get_update_fields(self):
        return ['content', 'vid_pic']

    def handle_model_history(self, instance, data_history):
        models.VidPicSubHistoryModel.objects.create(
            sub_model=instance,
            **data_history,
        )


#
class VidPicSubLikeViewLC(VidPicSubLikeView, VidPicSubLikeHistoryViewL, UserCreateLike):

    def get_queryset(self):
        return get_like_queryset(self.request, super().get_queryset())

    def get_instance_create(self):
        sub_id = self.request.data.get('vid_pic_sub_model')

        return self.queryset.get(sub_model=sub_id, profile_model=self.request.user.id)


#
class VidPicSubHistoryViewL(VidPicSubHistoryView, VidPicSubLikeHistoryViewL):
    pass

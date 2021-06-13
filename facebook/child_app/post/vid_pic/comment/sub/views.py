from rest_framework.generics import ListAPIView
#
from . import models, serizializers
#
from _common.views.user_create import UserCreateView, UserCreateLike
from _common.views.user_update import UserUpdateToHistoryView
from _common.views.user_delete import UserDestroyView


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


class VidPicSubLikeHistoryViewL(ListAPIView):

    def get_queryset(self):
        sub_id = self.request.query_params.get('vid_pic_sub_model')

        return self.queryset.filter(sub_model=sub_id)


# -------------


#
class VidPicSubViewLC(VidPicSubView, ListAPIView, UserCreateView):

    def get_queryset(self):
        comment_id = self.request.query_params.get('vid_pic_comment_model')

        return self.queryset.filter(comment_model=comment_id)


class VidPicSubViewUD(VidPicSubView, UserUpdateToHistoryView, UserDestroyView):

    @staticmethod
    def get_update_fields():
        return ['content', 'vid_pic']

    def handle_model_history(self, instance, data_history):
        models.VidPicSubHistoryModel.objects.create(
            sub_model=instance,
            **data_history,
        )


#
class VidPicSubLikeViewLC(VidPicSubLikeView, VidPicSubLikeHistoryViewL, UserCreateLike):

    def get_instance(self):
        sub_id = self.request.query_params.get('vid_pic_sub_model')

        return self.queryset.get(sub_model=sub_id, profile_model=self.request.user.id)


#
class VidPicSubHistoryViewL(VidPicSubHistoryView, VidPicSubLikeHistoryViewL):
    pass

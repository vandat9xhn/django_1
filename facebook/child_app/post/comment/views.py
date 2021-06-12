from rest_framework.generics import ListAPIView
#
from . import models, serializers
#
from _common.views.user_create import UserCreateView, UserCreateLike
from _common.views.user_update import UserUpdateToHistoryView
from _common.views.user_delete import UserDestroyView
from _common.views.facebook.post import FollowPostViewL

# Create your views here.


# ----------------


class CommentView:
    queryset = models.CommentModel.objects.all()
    serializer_class = serializers.CommentSerializer


class CmtLikeView:
    queryset = models.CmtLikeModel.objects.all()
    serializer_class = serializers.CmtLikeSerializer


class CmtHistoryView:
    queryset = models.CmtHistoryModel.objects.all()
    serializer_class = serializers.CmtHistorySerializer


# -------------


class CmtLikeHistoryViewL(ListAPIView):

    def get_queryset(self):
        comment_id = self.request.query_params.get('comment_model')

        return self.queryset.filter(comment_model=comment_id)


# ----------------


class CommentViewLC(CommentView, FollowPostViewL, UserCreateView):
    pass


class CommentViewUD(CommentView, UserUpdateToHistoryView, UserDestroyView):

    @staticmethod
    def get_update_fields():
        return ['content', 'vid_pic']

    @staticmethod
    def handle_model_history(instance, data_history):
        models.CmtHistoryModel.objects.create(
            comment_model=instance,
            **data_history,
        )


#
class CmtLikeViewLC(CmtLikeView, CmtLikeHistoryViewL, UserCreateLike):

    def get_instance(self):
        comment_id = self.request.query_params.get('comment_model')

        return self.queryset.get(comment_model=comment_id, profile_model=self.request.user.id)


#
class CmtHistoryViewL(CmtHistoryView, CmtLikeHistoryViewL):
    pass

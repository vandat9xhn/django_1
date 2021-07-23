#
from . import models, serializers
#
from _common.views.user_create import UserCreateLike
from _common.views.user_update import UserUpdateToHistoryView
from _common.views.user_delete import UserDestroyView
from _common.views.facebook.post import FollowPostViewL, FollowCommentViewL
from _common.views.facebook.post_create import CommentSubViewC

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


class CmtLikeHistoryViewL(FollowCommentViewL):

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset


# ----------------


class CommentViewLC(CommentView, FollowPostViewL, CommentSubViewC):
    pass


class CommentViewUD(CommentView, UserUpdateToHistoryView, UserDestroyView):

    @staticmethod
    def get_update_fields():
        return ['content', 'vid_pic']

    def handle_model_history(self, instance, data_history):
        models.CmtHistoryModel.objects.create(
            comment_model=instance,
            **data_history,
        )


#
class CmtLikeViewLC(CmtLikeView, CmtLikeHistoryViewL, UserCreateLike):

    def get_instance_create(self):
        comment_id = self.request.data.get('comment_model')

        return self.queryset.get(comment_model=comment_id, profile_model=self.request.user.id)


#
class CmtHistoryViewL(CmtHistoryView, CmtLikeHistoryViewL):
    pass

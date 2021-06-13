from rest_framework.generics import ListAPIView
#
from . import models, serizializers
#
from _common.views.user_create import UserCreateView, UserCreateLike
from _common.views.user_update import UserUpdateToHistoryView
from _common.views.user_delete import UserDestroyView

# Create your views here.


# -------------


class SubView:
    queryset = models.SubModel.objects.all()
    serializer_class = serizializers.SubSerializer


class SubLikeView:
    queryset = models.SubLikeModel.objects.all()
    serializer_class = serizializers.SubLikeSerializer


class SubHistoryView:
    queryset = models.SubHistoryModel.objects.all()
    serializer_class = serizializers.SubHistorySerializer


# -------------


class SubLikeHistoryViewL(ListAPIView):

    def get_queryset(self):
        sub_id = self.request.query_params.get('sub_model')

        return self.queryset.filter(sub_model=sub_id)


# -------------


#
class SubViewLC(SubView, ListAPIView, UserCreateView):

    def get_queryset(self):
        comment_id = self.request.query_params.get('comment_model')

        return self.queryset.filter(comment_model=comment_id)


class SubViewUD(SubView, UserUpdateToHistoryView, UserDestroyView):

    @staticmethod
    def get_update_fields():
        return ['content', 'vid_pic']

    def handle_model_history(self, instance, data_history):
        models.SubHistoryModel.objects.create(
            sub_model=instance,
            **data_history,
        )


#
class SubLikeViewLC(SubLikeView, SubLikeHistoryViewL, UserCreateLike):

    def get_instance(self):
        sub_id = self.request.query_params.get('sub_model')

        return self.queryset.get(sub_model=sub_id, profile_model=self.request.user.id)


#
class SubHistoryViewL(SubHistoryView, SubLikeHistoryViewL):
    pass

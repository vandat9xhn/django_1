from rest_framework.response import Response
from rest_framework import status
#
from . import models, serializers
#
from _common.views.facebook.post import FollowPostViewL, get_like_queryset
from _common.views.user_create import UserCreateLike, UserCreateShare


# -------------


class LikeView:
    queryset = models.LikeModel.objects.all()
    serializer_class = serializers.LikeSerializer


class ShareView:
    queryset = models.ShareModel.objects.all()
    serializer_class = serializers.ShareSerializer


# --------------


class LikeViewLC(LikeView, FollowPostViewL, UserCreateLike):

    def get_queryset(self):
        return get_like_queryset(self.request, super().get_queryset())

    def get_instance_create(self):
        return self.queryset.get(
            profile_model=self.request.user.id,
            post_model=self.request.data.get('post_model'),
        )


#
class ShareViewLC(ShareView, FollowPostViewL, UserCreateShare):

    def has_permission_create(self):
        return super().has_permission_create()

    @staticmethod
    def get_max_share():
        return 5

    def get_count_user_share(self):
        post_id = self.request.data.get('post_model')

        return self.queryset.get(profile_model=self.request.user.id, post_model=post_id).count

    def handle_create_share(self):
        user_id = self.request.user.id
        post_id = self.request.data.get('post_model')

        serializer = self.get_serializer(data={
            'profile_model': user_id,
            'post_model': post_id,
            'count': 1,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK)

    def handle_update_share(self):
        user_id = self.request.user.id
        post_id = self.request.data.get('post_model')

        share_user_model = self.queryset.get(profile_model=user_id, post_model=post_id)
        share_user_model.count += 1
        share_user_model.save()

        return Response(status=status.HTTP_200_OK)

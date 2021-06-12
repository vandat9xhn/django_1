from rest_framework.response import Response
from rest_framework import status
#
from . import models, serializers
#
from ...post.models import PostModel
#
from user_profile.models import ProfileModel
#
from _common.views.facebook.post import FollowPostViewL
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
    pass


#
class ShareViewLC(ShareView, FollowPostViewL, UserCreateShare):

    @staticmethod
    def get_max_share():
        return 5

    def get_count_user_share(self):
        post_id = self.request.data.get('post_model')

        return self.queryset.get(profile_model=self.request.user.id, post_model=post_id).count

    def handle_create_share(self, count_user_share):
        user_id = self.request.user.id
        post_id = self.request.data.get('post_model')

        if count_user_share == 0:
            models.ShareModel.objects.create(
                profile_model=ProfileModel.objects.get(id=user_id),
                post_model=PostModel.objects.get(id=post_id),
                count=1,
            )
        else:
            share_user_model = self.queryset.get(profile_model=user_id, post_model=post_id)
            share_user_model.count += 1
            share_user_model.save()

        return Response(status=status.HTTP_200_OK)

from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
#
from . import models, serializers
#
from _common.views.facebook.post import FollowPostViewL, FollowVidPicViewL, get_like_queryset
from _common.views.user_create import UserCreateLike, UserCreateShare
from _common.views.user_update import UserUpdateToHistoryView
from _common.views.user_delete import UserDestroyView


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

    def get_queryset(self):
        return get_like_queryset(self.request, super().get_queryset())

    def get_instance_create(self):
        vid_pic_id = self.request.query_params['vid_pic_model']

        return self.queryset.get(profile_model=self.request.user.id, vid_pic_model=vid_pic_id)


#
class VidPicShareViewLC(VidPicShareView, FollowVidPicViewL, UserCreateShare):

    @staticmethod
    def get_max_share():
        return 5

    def get_count_user_share(self):
        user_id = self.request.user.id
        vid_pic_id = self.request.data.get('vid_pic_model')

        return self.queryset.get(profile_model=user_id, vid_pic_model=vid_pic_id).count

    def has_permission_create(self):
        return super().has_permission_create()

    def handle_create_share(self):
        user_id = self.request.user.id
        vid_pic_id = self.request.data.get('vid_pic_model')

        serializer = self.get_serializer(data={
            'profile_model': user_id,
            'vid_pic_model': vid_pic_id,
            'count': 1,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def handle_update_share(self):
        user_id = self.request.user.id

        instance = self.queryset.get(profile_model=user_id)
        instance.count += 1
        instance.save()

        return Response(status=status.HTTP_200_OK)


#
class VidPicHistoryViewL(VidPicHistoryView, FollowVidPicViewL):
    pass

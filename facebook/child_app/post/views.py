from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
#
from . import models, serializers
#
from .vid_pic.models import VidPicModel
from .history.models import HistoryModel, HistoryVidPicCreateModel, HistoryVidPicDelModel
#
from friend.models import get_friend_id_arr
from user_profile.models import ProfileModel
from user_profile.child_app.picture.models import PictureModel, CoverModel
#
from _common.views.user_delete import UserDestroyView
from _common.views.user_update import UserUpdateToHistoryView, UserUpdateView
from _common.views.permission_list import PermissionViewL, PermissionViewR

# --------------


class PostView:
    queryset = models.PostModel.objects.all()
    serializer_class = serializers.PostSerializer


# --------------


class PostViewL(PostView, PermissionViewL, CreateAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        request_from = self.request.query_params.get('request_from')
        queryset = self.queryset.none()

        if request_from == 'new_feed':
            friend_id_arr = get_friend_id_arr(user_id)

            queryset = self.queryset.filter(
                profile_model__in=[*friend_id_arr, user_id]
            )

        elif request_from == 'user':
            profile_id = self.request.query_params.get('profile_model')

            queryset = self.queryset.filter(
                profile_model=profile_id
            )

        elif request_from == 'group':
            post_to_id = self.request.query_params.get('post_to_id')

            queryset = self.queryset.filter(post_to_where='group', post_to_id=post_to_id)

        return queryset.order_by('-updated_time')

    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        type_post = request.data.get('type_post')

        post_to_where = request.data.get('post_to_where')
        post_to_id = request.data.get('post_to_id')
        content = request.data.get('content')

        if not post_to_where:
            post_to_where = 'user'

        if not post_to_id:
            post_to_id = user_id

        serializer = self.get_serializer(data={
            'profile_model': user_id,
            'type_post': type_post,
            'post_to_where': post_to_where,
            'post_to_id': post_to_id,
            'content': content,
        })
        serializer.is_valid(raise_exception=True)

        #
        if type_post == 'share':
            serializer.save()

        elif type_post == 'post':
            vid_pics = request.data.getlist('vid_pics')

            if len(vid_pics) == 0 and not content:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            new_post_model = serializer.save()

            VidPicModel.objects.bulk_create([
                VidPicModel(
                    post_model=new_post_model,
                    vid_pic=vid_pic,
                ) for vid_pic in vid_pics
            ])

        elif type_post == 'picture' or type_post == 'cover':
            vid_pic = request.data.getlist('vid_pic')

            if not vid_pic:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            new_post_model = serializer.save()
            profile_model = ProfileModel.objects.get(id=user_id)

            new_vid_pic_model = VidPicModel.objects.create(
                post_model=new_post_model,
                vid_pic=vid_pic,
            )

            if type_post == 'picture':
                model_pic = PictureModel
            else:
                model_pic = CoverModel

            model_pic.objects.create(
                profile_model=profile_model,
                url=new_vid_pic_model.vid_pic,
                post_model=new_post_model,
                is_active=True,
            )

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class PostViewRUD(PostView, PermissionViewR, UserUpdateToHistoryView, UserDestroyView):

    @staticmethod
    def get_update_fields():
        return ['content']

    def handle_model_history(self, instance, data_history):
        his_model = HistoryModel.objects.create(
            post_model=instance,
            **data_history,
        )
        if instance.type_post == 'post':
            create_vid_pics = self.request.data.getlist('create_vid_pics')
            delete_vid_pics = self.request.data.getlist('delete_vid_pics')

            self.handle_his_vid_pics(his_model, create_vid_pics, delete_vid_pics)

    def handle_fail_update(self, instance, data_history):
        if instance.type_post != 'post':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        create_vid_pics = self.request.data.getlist('create_vid_pics')
        delete_vid_pics = self.request.data.getlist('delete_vid_pics')

        if len(create_vid_pics) + len(delete_vid_pics) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        his_model = HistoryModel.objects.create(
            post_model=instance,
        )

        self.handle_his_vid_pics(his_model, create_vid_pics, delete_vid_pics)

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def handle_his_vid_pics(his_model, create_vid_pics, delete_vid_pics):
        if len(create_vid_pics):
            HistoryVidPicCreateModel.objects.bulk_create([
                HistoryVidPicCreateModel(
                    his_model=his_model,
                    vid_pic=vid_pic,
                ) for vid_pic in create_vid_pics
            ])

        if len(delete_vid_pics):
            HistoryVidPicDelModel.objects.bulk_create([
                HistoryVidPicDelModel(
                    his_model=his_model,
                    vid_pic=vid_pic,
                ) for vid_pic in create_vid_pics
            ])


class PostPerMissionViewU(PostView, UserUpdateView):

    def update(self, request, *args, **kwargs):
        new_permission = request.data.get('permission')

        instance = self.get_object()
        serializer = self.get_serializer(instance, data={'permission': new_permission}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

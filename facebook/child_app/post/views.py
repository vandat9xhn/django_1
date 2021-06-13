from django.core.exceptions import ObjectDoesNotExist
#
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
#
from . import models, serializers
#
from .vid_pic.models import VidPicModel
from .history.models import HistoryModel, HistoryVidPicCreateModel, HistoryVidPicDelModel
#
from friend.models import get_friend_id_arr, friend_relative_num
from user_profile.models import ProfileModel
from user_profile.child_app.picture.models import PictureModel, CoverModel
#
from _common.views.user_delete import UserDestroyView
from _common.views.user_update import UserUpdateToHistoryView, UserUpdateView
from _common.views.permission_view import PermissionViewR
from _common.views.active_view import change_active_instance


# --------------


class PostView:
    queryset = models.PostModel.objects.all()
    serializer_class = serializers.PostSerializer


# --------------


def has_permission_post_create(post_to_where, post_to_id, user_id):
    return True


def handle_his_vid_pics(user_id, his_model, create_vid_pics, create_vid_pic_contents, delete_vid_pic_ids):
    if len(create_vid_pics):
        HistoryVidPicCreateModel.objects.bulk_create([
            HistoryVidPicCreateModel(
                his_model=his_model,
                vid_pic=vid_pic,
            ) for vid_pic in create_vid_pics
        ])

        VidPicModel.objects.bulk_create([
            VidPicModel(
                post_model=his_model.post_model,
                vid_pic=vid_pic,
                content=content,
            ) for vid_pic, content in zip(create_vid_pics, create_vid_pic_contents)
        ])

    delete_vid_pics = []

    for pk_del in delete_vid_pic_ids:
        vid_pic_model = VidPicModel.objects.get(id=pk_del)
        if vid_pic_model.post_model.profile_model.id == user_id:
            delete_vid_pics += vid_pic_model.vid_pic.url
            print(delete_vid_pics)
        else:
            return

    if len(delete_vid_pics):
        HistoryVidPicDelModel.objects.bulk_create([
            HistoryVidPicDelModel(
                his_model=his_model,
                vid_pic=vid_pic,
            ) for vid_pic in create_vid_pics
        ])
    VidPicModel.objects.filter(id__in=delete_vid_pic_ids).delete()


# --------------


class PostViewLC(PostView, ListCreateAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        request_from = self.request.query_params.get('request_from')
        queryset = self.queryset.none()

        if request_from == 'new_feed':
            friend_id_arr = get_friend_id_arr(user_id)

            queryset = self.queryset.filter(
                profile_model__in=[*friend_id_arr, user_id],
                permission__lte=2,
            )

        elif request_from == 'user':
            profile_id = self.request.query_params.get('profile_model')

            relative = friend_relative_num(
                self.request.user.id,
                profile_id,
            )

            queryset = self.queryset.filter(
                profile_model=profile_id,
                permission__lte=relative,
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

        if not has_permission_post_create(post_to_where, post_to_id, user_id):
            return Response(status=status.HTTP_400_BAD_REQUEST)

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
            post_share_id = request.data.get('post_share_model')

            try:
                post_share_model = models.PostModel.objects.get(id=post_share_id)
                new_post_model = serializer.save()

                models.PostShareModel.objects.create(
                    post_model=new_post_model,
                    post_share_model=post_share_model,
                )
            except ObjectDoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        elif type_post == 'post':
            vid_pics = request.data.getlist('vid_pics')
            content_vid_pics = request.data.getlist('content_vid_pics')

            if len(vid_pics) == 0 and not content:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            new_post_model = serializer.save()

            # VidPicModel.objects.bulk_create([
            #     VidPicModel(
            #         post_model=new_post_model,
            #         vid_pic=vid_pic,
            #         content=content_vid_pic,
            #     ) for vid_pic, content_vid_pic in zip(vid_pics, content_vid_pics)
            # ])

            vid_pic_count = len(vid_pics)

            if vid_pic_count > 0:
                VidPicModel.objects.bulk_create([
                    VidPicModel(
                        post_model=new_post_model,
                        vid_pic=vid_pics[i],
                        content=content_vid_pics[i],
                    ) for i in range(vid_pic_count)
                ])

        elif type_post == 'picture' or type_post == 'cover':
            vid_pic = request.data.get('vid_pic')

            if not vid_pic:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            new_post_model = serializer.save()
            profile_model = ProfileModel.objects.get(id=user_id)

            new_vid_pic_model = VidPicModel.objects.create(
                post_model=new_post_model,
                vid_pic=vid_pic,
                content='',
            )

            if type_post == 'picture':
                model_pic = PictureModel
            else:
                model_pic = CoverModel

            change_active_instance(model_pic.objects.filter(profile_model=profile_model))

            model_pic.objects.create(
                profile_model=profile_model,
                url=new_vid_pic_model.vid_pic.url,
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
            user_id = self.request.user.id
            create_vid_pics = self.request.data.getlist('create_vid_pics')
            create_vid_pic_contents = self.request.data.getlist('create_vid_pic_contents')
            delete_vid_pics = self.request.data.getlist('delete_vid_pics')

            if instance.content == '':
                if len(create_vid_pics) == 0:
                    if len(delete_vid_pics) == VidPicModel.objects.filter(post_model=instance.id).count():
                        instance.delete()
                        return Response(status=status.HTTP_204_NO_CONTENT)

            handle_his_vid_pics(user_id, his_model, create_vid_pics, create_vid_pic_contents, delete_vid_pics)

    def handle_fail_update(self, instance, data_history):
        if instance.type_post != 'post':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user_id = self.request.user.id
        create_vid_pics = self.request.data.getlist('create_vid_pics')
        create_vid_pic_contents = self.request.data.getlist('create_vid_pic_contents')
        delete_vid_pic_ids = self.request.data.getlist('delete_vid_pic_ids')

        if len(create_vid_pics) + len(delete_vid_pic_ids) == 0:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        his_model = HistoryModel.objects.create(
            post_model=instance,
        )

        handle_his_vid_pics(user_id, his_model, create_vid_pics, create_vid_pic_contents, delete_vid_pic_ids)

        return Response(status=status.HTTP_200_OK)

    def has_permission_delete(self):
        user_id = self.request.user.id
        instance = self.get_object()
        post_to_where = instance.post_to_where
        post_to_id = instance.post_to_id
        profile_model = instance.profile_model

        if post_to_where == 'user':
            if post_to_id == user_id:
                return True

            elif profile_model.id == user_id:
                return True

        return False


class PostPerMissionViewU(PostView, UserUpdateView):

    def update(self, request, *args, **kwargs):
        new_permission = request.data.get('permission')
        instance = self.get_object()

        if not self.has_permission():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if new_permission is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if int(new_permission) == instance.permission:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data={'permission': new_permission}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

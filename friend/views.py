from django.db.models import Q
#
from rest_framework.generics import ListAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
#
from user_profile.models import PersonalSettingModel, ProfileModel
# 
from . import serializers, models


#
from _common.views.user_update import UserUpdateView


# Create your views here.


# -----------------


class FriendView:
    queryset = models.FriendModel.objects.all()
    serializer_class = serializers.FriendSerializer


class AddFriendView:
    queryset = models.AddFriendModel.objects.all()
    serializer_class = serializers.AddFriendSerializer


# -------------------


#
class FriendMayKnowViewL(FriendView, ListAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        # friend_id_arr = models.get_friend_id_arr(user_id)

        # return self.queryset.filter(
        #     Q(requester__in=friend_id_arr) |
        #     Q(receiver__in=friend_id_arr)
        # ).exclude(profile_model=user_id).exclude(friend_model=user_id)

        return self.queryset.exclude(profile_model=user_id).exclude(friend_model=user_id)


class FriendViewLC(FriendView, ListCreateAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        friend_id = self.request.query_params.get('profile_model') or user_id

        permission = PersonalSettingModel.objects.get(profile_model=friend_id).permission_see_friend
        has_permission = models.friend_has_permission(user_id, friend_id, permission)

        if has_permission:
            return self.queryset.filter(profile_model=friend_id)

        return []

    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        friend_id = request.data.get('profile_model')

        add_friend_model = models.AddFriendModel.objects.filter(profile_model=friend_id, friend_model=user_id)

        if add_friend_model.count() == 1:
            models.FriendModel.objects.create(
                profile_model=ProfileModel.objects.get(id=friend_id),
                friend_model=ProfileModel.objects.get(id=user_id)
            )

            models.FriendModel.objects.create(
                profile_model=ProfileModel.objects.get(id=user_id),
                friend_model=ProfileModel.objects.get(id=friend_id)
            )

            add_friend_model.delete()

            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class FriendViewU(FriendView, UserUpdateView):

    def perform_update(self, serializer):
        serializer.save(
            profile_model=self.get_object().profile_model,
            friend_model=self.get_object().friend_model
        )


class FriendViewD(FriendView, DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        user_id = request.user.id
        friend_id = request.data['friend_model']
        self.queryset.filter(
            Q(profile_model=user_id, friend_model=friend_id) |
            Q(profile_model=friend_id, friend_model=user_id)
        ).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


#
class AddFriendCountNewView(AddFriendView, ListAPIView):

    def get(self, request, *args, **kwargs):

        count_new = self.queryset.filter(receiver=request.user.id, has_seen=False).count()
        return Response(data={'count': count_new})


class AddFriendViewLC(AddFriendView, ListCreateAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        friend_request = self.request.query_params.get('friend_request')

        if friend_request == 'sent':
            return self.queryset.filter(requester=user_id)

        if friend_request == 'requested':
            return self.queryset.filter(receiver=user_id)

        return []

    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        friend_id = request.data.get('profile_model')
        permission = PersonalSettingModel.objects.get(profile_model=friend_id).permission_add_friend
        relative = models.friend_relative_num(user_id, friend_id)

        #
        if relative >= 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if relative < permission:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if models.AddFriendModel.objects.filter(
                Q(requester=friend_id, receiver=user_id) |
                Q(requester=user_id, receiver=friend_id)
        ).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        #
        models.AddFriendModel.objects.create(
            requester=ProfileModel.objects.get(id=user_id),
            receiver=ProfileModel.objects.get(id=friend_id)
        )

        return Response(status=status.HTTP_201_CREATED)


class AddFriendViewD(AddFriendView, DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        user_id = request.user.id
        friend_id = request.data['friend_model']
        self.queryset.filter(
            Q(requester=user_id, receiver=friend_id) |
            Q(requester=friend_id, receiver=user_id)
        ).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class FriendRemoveViewD(AddFriendView, DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        user_id = request.user.id
        friend_id = kwargs['pk']

        if models.friend_relative_num(user_id, friend_id) >= 2:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        self.queryset.filter(
            Q(profile_model=user_id, friend_model=friend_id) | Q(profile_model=friend_id, friend_model=user_id)
        ).delete()

        models.FriendRemoveModel.objects.create(
            profile_model=ProfileModel.objects.get(id=user_id),
            friend_model=ProfileModel.objects.get(id=friend_id)
        )

        return Response(status=status.HTTP_200_OK)

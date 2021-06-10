from django.db.models import Q
#
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status
#
from user_profile.models import PersonalSettingModel, ProfileModel
# 
from . import serializers, models


# Create your views here.


# -----------------


class FriendView:
    queryset = models.FriendModel.objects.all()
    serializer_class = serializers.FriendSerializer


class AddFriendView:
    queryset = models.AddFriendModel.objects.all()
    serializer_class = serializers.AddFriendSerializer


# -------------------


class FriendAddFriendViewD(DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        user_id = request.user.id
        instance = self.get_object()

        if user_id == instance.requester.id or user_id == instance.receiver.id:
            return super().delete(request, *args, **kwargs)

        return Response(status=status.HTTP_400_BAD_REQUEST)


# -------------------


#
class FriendMayKnowViewL(FriendView, ListAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        friend_id_arr = models.get_friend_id_arr(user_id)

        return self.queryset.filter(
            Q(requester__in=friend_id_arr) |
            Q(receiver__in=friend_id_arr)
        ).exclude(requester=user_id).exclude(receiver=user_id)


class FriendViewLC(FriendView, ListCreateAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        friend_id = self.request.query_params.get('profile_model')

        if friend_id is None:
            friend_id = user_id

        permission = PersonalSettingModel.objects.get(profile_model=friend_id).permission_see_friend

        has_permission = models.friend_has_permission(user_id, friend_id, permission)

        if has_permission:
            return self.queryset.filter(Q(requester=friend_id) | Q(receiver=friend_id))

        return self.queryset.none()

    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        friend_id = request.data.get('profile_model')

        add_friend_model = models.AddFriendModel.objects.filter(requester=friend_id, receiver=user_id)

        if add_friend_model.count() == 1:
            models.FriendModel.objects.create(
                requester=ProfileModel.objects.get(id=friend_id),
                receiver=ProfileModel.objects.get(id=user_id)
            )

            add_friend_model.delete()

            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class FriendViewD(FriendView, FriendAddFriendViewD):
    pass


# 
class AddFriendViewLC(AddFriendView, ListCreateAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        user_request = self.request.query_params.get('user_request')

        if user_request == 'requester':
            return self.queryset.filter(requester=user_id)

        if user_request == 'receiver':
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


class AddFriendViewD(AddFriendView, FriendAddFriendViewD):
    pass

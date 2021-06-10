from django.core.exceptions import ObjectDoesNotExist
#
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
#
from user_profile.models import ProfileModel
from _common.views.active_view import change_active_instance

#


class UserUpdateView(UpdateAPIView):

    def update(self, request, *args, **kwargs):
        user = request.user
        profile_id = self.get_object().profile_model.id

        if user.id == profile_id:
            return super().update(request, *args, **kwargs)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save(profile_model=ProfileModel.objects.get(id=self.request.user.id))


class UserUpdateOnlyOne(UserUpdateView):

    def get_object(self):
        return self.queryset.get(profile_model=self.request.user.id)


class UserUpdateOrCreate(UserUpdateView):

    def update(self, request, *args, **kwargs):
        try:
            super().update(request, *args, **kwargs)

        except ObjectDoesNotExist:
            self.queryset.create(**request.data)

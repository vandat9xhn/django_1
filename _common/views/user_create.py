from django.core.exceptions import ObjectDoesNotExist
#
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
#
from user_profile.models import ProfileModel
#


class UserCreateView(CreateAPIView):

    def perform_create(self, serializer):
        serializer.save(profile_model=ProfileModel.objects.get(id=self.request.user.id))


class UserCreateOnlyOne(UserCreateView):

    def create(self, request, *args, **kwargs):
        try:
            instance = self.get_instance()
            self.handle_exists(instance)

            return Response(status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return super().create(request, *args, **kwargs)

    def get_instance(self):
        return self.queryset.get(profile_model=self.request.user.id)

    def handle_exists(self, instance):
        pass

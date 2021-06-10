from django.core.exceptions import ObjectDoesNotExist
#
from rest_framework.generics import CreateAPIView
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
            instance.delete()

        except ObjectDoesNotExist:
            super().create(request, *args, **kwargs)

    def get_instance(self):
        return self.queryset.get(profile_model=self.request.user.id)

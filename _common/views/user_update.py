from django.core.exceptions import ObjectDoesNotExist
#
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status


#


class UserUpdateView(UpdateAPIView):

    def update(self, request, *args, **kwargs):
        if self.has_permission():
            return super().update(request, *args, **kwargs)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save(profile_model=self.get_object().profile_model)

    def has_permission(self):
        user_id = self.request.user.id
        profile_id = self.get_object().profile_model.id

        if user_id == profile_id:
            return True

        return False


class UserUpdateOnlyOne(UserUpdateView):

    def get_object(self):
        return self.queryset.get(profile_model=self.request.user.id)


class UserUpdateOrCreate(UserUpdateView):

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)

        except ObjectDoesNotExist:
            return self.queryset.create(**request.data)


#
class UserUpdateToHistoryView(UpdateAPIView):

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        profile_model = self.get_profile_model()
        user_id = request.user.id

        if profile_model.id != user_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        data_history = {}
        data_new = {
            profile_model: user_id,
        }
        update_fields = self.get_update_fields()

        if not update_fields:
            update_fields = []

        for field in update_fields:
            if field in data:
                new_value = data[field]
                old_value = getattr(instance, field)

                if new_value != old_value:
                    data_history[field] = old_value
                    data_new[field] = new_value

        if data_history == {}:
            return self.handle_fail_update(instance, data_history)

        serializer = self.get_serializer(instance, data=data_new, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        self.handle_model_history(instance, data_history)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(status=status.HTTP_200_OK)

    def get_profile_model(self):
        return self.get_object().profile_model

    def perform_update(self, serializer):
        serializer.save()

    @staticmethod
    def get_update_fields():
        return ['']

    def handle_model_history(self, instance, data_history):
        pass

    def handle_fail_update(self, instance, data_history):
        return Response(status=status.HTTP_400_BAD_REQUEST)

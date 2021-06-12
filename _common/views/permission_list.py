from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
#
from friend.models import friend_relative_num


#


class PermissionViewL(ListAPIView):

    def get_queryset(self):
        return self.queryset.filter(permission__lte=friend_relative_num(
            self.request.user.id,
            int(self.request.query_params.get('profile_model'))
        ))


class PermissionViewR(RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        relative = friend_relative_num(
            self.request.user.id,
            int(self.request.query_params.get('profile_model'))
        )

        if relative < self.get_object().permission:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return super().retrieve(request, *args, **kwargs)

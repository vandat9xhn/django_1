from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
#
from friend.models import friend_relative_num


#


class PermissionViewR(RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        if self.has_permission_retrieve():
            return super().retrieve(request, *args, **kwargs)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def has_permission_retrieve(self):
        relative = friend_relative_num(
            self.request.user.id,
            self.get_profile_id()
        )

        return relative >= self.get_permission_num()

    def get_profile_id(self):
        return 0

    def get_permission_num(self):
        return self.get_object().permission

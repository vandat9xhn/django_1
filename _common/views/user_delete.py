from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework import status


#


class UserDestroyView(DestroyAPIView):

    def delete(self, request, *args, **kwargs):
        if self.has_permission_delete():
            return super().delete(request, *args, **kwargs)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def has_permission_delete(self):
        if self.request.user.id == self.get_object().profile_model.id:
            return True

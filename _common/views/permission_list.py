from rest_framework.generics import ListAPIView
#
from friend.models import friend_relative_num


#


class PermissionViewL(ListAPIView):

    def get_queryset(self):
        return self.queryset.filter(permission__lte=friend_relative_num(
            self.request.user,
            + self.request.query_params.get('profile_model')
        ))

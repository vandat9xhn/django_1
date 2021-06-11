from rest_framework.generics import ListAPIView


#


class UserListView(ListAPIView):

    def get_queryset(self):
        user_id = self.request.user.id

        return self.queryset.filter(profile_model=user_id)

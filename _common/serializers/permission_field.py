from _common.serializers.data_field import DataSerializerR, DataSerializerL
#
from friend.models import friend_has_permission, friend_relative_num


#


class DataPermissionSerializerR(DataSerializerR):

    def get_data_permission_r(self, serializer, queryset, change_data_not_permission):
        request = self.context['request']
        permission = queryset.permission
        user = request.user
        friend_id = request.query_params.get('pk')

        if friend_id is None:
            friend_id = request.data.get('profile_model')

        data = self.get_data_r(
            serializer,
            queryset
        )

        if not friend_has_permission(user, + friend_id, permission):
            change_data_not_permission(data)

        return data


class DataPermissionSerializerL(DataSerializerL):

    def get_data_permission_l(self, serializer, queryset, friend_id):
        request = self.context['request']
        user = request.user

        relative = friend_relative_num(user, int(friend_id))

        return self.get_data_l(
            serializer,
            queryset.filter(permission__lte=relative)
        )

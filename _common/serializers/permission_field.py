from _common.serializers.data_field import DataSerializerR, DataSerializerL
#
from friend.models import friend_has_permission, friend_relative_num


#


class DataPermissionSerializerR(DataSerializerR):

    def get_data_permission_r(self, serializer, queryset, friend_id, permission):
        request = self.context['request']
        user_id = request.user.id

        if not friend_has_permission(user_id, friend_id, permission):
            return {}

        data = self.get_data_r(
            serializer,
            queryset
        )

        return data


class DataPermissionSerializerL(DataSerializerL):

    def get_data_permission_l(self, serializer, queryset, friend_id):
        relative = friend_relative_num(self.context['request'].user.id, int(friend_id))

        return self.get_data_l(
            serializer,
            queryset.filter(permission__lte=relative)
        )

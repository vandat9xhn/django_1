#
from friend.models import friend_has_permission
#
from _common.serializers.data_field import FieldSerializer


#


class InteractiveSerializer(FieldSerializer):

    def get_fields(self):
        if not friend_has_permission(
                self.context['request'].user.id,
                self.instance.profile_model.id,
                self.instance.profile_model.personalsettingmodel.permission_see_interactive
        ):
            return []

        return super().get_fields()

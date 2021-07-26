from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.custom_field import FieldSerializer
#
from user_profile.serializers import ProfileBaseSerializer

#


class DataProfileSerializer(FieldSerializer):
    # pass
    user = SerializerMethodField()

    def get_user(self, instance):

        return ProfileBaseSerializer(
            instance=instance.profile_model,
            many=False,
            context=self.context,
        ).data

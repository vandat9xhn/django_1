from rest_framework.serializers import SerializerMethodField, ModelSerializer
#
from data_field import DataSerializerR, DataSerializerL
#
from user_profile.serializers import ProfileSerializer, ProfileModel
from friend.models import friend_has_permission, friend_relative_num


#


class DataProfileSerializer(DataSerializerR):
    user = SerializerMethodField('get_user')

    def get_user(self):
        return self.get_data_r(ProfileSerializer, ProfileModel)

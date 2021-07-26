from rest_framework.serializers import SerializerMethodField
# 
from _common.serializers import data_field
# 
from user_profile.serializers import ProfileBaseSerializer
from user_profile.models import ProfileModel
# 
from . import models

# 


class FriendSerializer(data_field.DataSerializerR):
    name_field = 'friend'
    # 
    friend = SerializerMethodField()
    
    class Meta:
        model = models.FriendModel
        fields = '__all__'
        
    def get_friend(self, instance):

        return self.get_data_r(
            ProfileBaseSerializer,
            ProfileModel.objects.get(id=instance.friend_model.id)
        )


class AddFriendSerializer(data_field.DataSerializerR):
    name_field = 'add_friend'
    #
    requester = SerializerMethodField()
    receiver = SerializerMethodField()

    class Meta:
        model = models.AddFriendModel
        fields = '__all__'

    def get_requester(self, instance):

        return self.get_data_r(
            ProfileBaseSerializer,
            ProfileModel.objects.get(id=instance.requester.id)
        )

    def get_receiver(self, instance):

        return self.get_data_r(
            ProfileBaseSerializer,
            ProfileModel.objects.get(id=instance.receiver.id)
        )

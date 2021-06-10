from rest_framework.serializers import SerializerMethodField
# 
from _common.serializers import data_field
# 
from user_profile.serializers import ProfileSerializer
from user_profile.models import ProfileModel
# 
from . import models

# 


class FriendSerializer(data_field.DataSerializerR):
    name_field = 'friend[]'
    # 
    friend = SerializerMethodField()
    
    class Meta:
        model = models.FriendModel
        fields = ('id', 'friend')
        
    def get_friend(self, instance):
        user_id = self.context['request'].query_params.get('profile_model')
        requester_id = instance.requester.id
        
        if user_id is None:
            user_id = self.context['request'].user.id
        
        if user_id == requester_id:
            friend_id = instance.receiver.id
        else:
            friend_id = requester_id
        
        return self.get_data_r(
            ProfileSerializer,
            ProfileModel.objects.get(id=friend_id)
        )


class AddFriendSerializer(data_field.DataSerializerR):
    name_field = 'add_friend[]'
    # 
    user_requester = SerializerMethodField()
    user_receiver = SerializerMethodField()

    class Meta:
        model = models.AddFriendModel
        fields = '__all__'

    def get_user_requester(self, instance):

        return self.get_data_r(
            ProfileSerializer,
            ProfileModel.objects.get(id=instance.requester.id)
        )
    
    def get_user_receiver(self, instance):

        return self.get_data_r(
            ProfileSerializer,
            ProfileModel.objects.get(id=instance.receiver.id)
        )

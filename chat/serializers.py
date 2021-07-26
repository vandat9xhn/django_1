from rest_framework.serializers import SerializerMethodField
#
from . import models
#
from _common.serializers.data_field import ArrWithCountSerializer
from _common.serializers.data_user import DataProfileSerializer
from _common.serializers.custom_field import FieldSerializer

#


class TimelineSerializer(FieldSerializer):
    name_field = 'room_timeline'
    
    class Meta:
        model = models.TimelineModel
        fields = '__all__'


class RoomUserSerializer(DataProfileSerializer):
    name_field = 'room_users'

    class Meta:
        model = models.RoomUserModel
        fields = '__all__'


class VidPicSerializer(FieldSerializer):
    name_field = 'room_vid_pics'

    class Meta:
        model = models.VidPicModel
        fields = '__all__'


class LikeSerializer(DataProfileSerializer):
    name_field = 'room_likes'

    class Meta:
        model = models.LikeModel
        fields = '__all__'


class MessageSerializer(ArrWithCountSerializer):
    name_field = 'room_messages'
    #
    vid_pic_obj = SerializerMethodField()
    like_obj = SerializerMethodField()

    class Meta:
        model = models.MessageModel
        fields = '__all__'

    def get_vid_pic_obj(self, instance):

        return self.get_arr_with_count(
            VidPicSerializer,
            models.VidPicModel.objects.filter(mess_model=instance.id),
            4
        )
    
    @staticmethod
    def get_like_obj(instance):
        type_like_arr = models.LikeModel.objects.filter(
            mess_model=instance.id
        ).order_by('type_like').values_list('type_like', flat=True)
        
        return {
            'distinct_user_like_arr': type_like_arr,
            'count': len(type_like_arr),
        }


class RoomSerializer(FieldSerializer):
    name_field = 'rooms'
    #
    user_obj = SerializerMethodField()
    message_obj = SerializerMethodField()
    count_new = SerializerMethodField()

    class Meta:
        model = models.RoomModel
        fields = '__all__'

    def get_user_obj(self, instance):
        queryset = models.RoomUserModel.objects.filter(room_model=instance.room_chat)
        
        return {
            'data': RoomUserSerializer(
                instance=queryset,
                many=True,
                context=self.context
            ).data,
            'count': queryset.count(),
        }

    def get_message_obj(self, instance):
        request = self.context['request']
        message_page = request.query_params.get('message_page') or 1

        message_instance = models.MessageModel.objects.filter(room_model=instance.room_chat)
        count = message_instance.count()

        return {
            'data': MessageSerializer(
                instance=message_instance.order_by('-created_time'),
                many=True,
                context=self.context
            ).data[0:int(message_page)],
            'count': count,
        }

    def get_count_new(self, instance):
        request = self.context['request']
        room_user_instance = models.RoomUserModel.objects.get(
            profile_model=request.user.id,
            room_model=instance.room_chat
        )

        return room_user_instance.last_mess - room_user_instance.last_receive

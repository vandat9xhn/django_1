from django.db.models import F
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
# 
from . import models, serializers

# Create your views here.


# ----------


def is_user_in_room(user_id, room_chat):
    return models.RoomUserModel.objects.filter(
        profile_model=user_id,
        room_model=room_chat,
    ).exists()


# ----------


class RoomView:
    queryset = models.RoomModel.objects.all()
    serializer_class = serializers.RoomSerializer


class RoomUserView:
    queryset = models.RoomUserModel.objects.all()
    serializer_class = serializers.RoomUserSerializer
    

class TimelineView:
    queryset = models.TimelineModel
    serializer_class = serializers.TimelineSerializer
    

class MessageView:
    queryset = models.MessageModel
    serializer_class = serializers.MessageSerializer


class VidPicView:
    queryset = models.VidPicModel
    serializer_class = serializers.VidPicSerializer


class LikeView:
    queryset = models.LikeModel
    serializer_class = serializers.LikeSerializer
    

# ----------


class FollowRoomViewL(ListAPIView):
    
    def get_queryset(self):
        room_chat = self.request.query_params['room_chat']
        if not is_user_in_room(self.request.user.id, room_chat):
            return []

        return self.queryset.filter(room_model=room_chat)


class FollowMessageViewL(ListAPIView):

    def get_queryset(self):
        user_id = self.request.user.id
        mess_id = self.request.query_params['mess_model']
        room_chat = models.MessageModel.objects.get(id=mess_id).room_model.room_chat

        if not is_user_in_room(user_id, room_chat):
            return []

        return self.queryset.filter(mess_model=mess_id)


# ----------


class RoomViewL(RoomView, ListAPIView):
    
    def get_queryset(self):
        user_id = self.request.user.id
        room_chat_arr = models.RoomUserModel.objects.filter(
            profile_model=user_id
        ).values_list('room_model', flat=True)

        print(room_chat_arr)
        
        return self.queryset.filter(room_chat__in=room_chat_arr)


class RoomCountView(RoomUserView, ListAPIView):

    def get(self, request, *args, **kwargs):

        count_new = self.queryset.filter(
            profile_model=request.user.id,
            last_mess__gt=F('last_receive')
        ).count()

        return Response(data={'count': count_new})
    
    
class RoomViewR(RoomView, RetrieveAPIView):
    
    def get(self, request, *args, **kwargs):
        if not is_user_in_room(request.user.id, kwargs['room_chat']):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return super().get(request, *args, **kwargs)
    

class TimelineViewL(TimelineView, FollowRoomViewL):
    pass


class MessageViewLC(MessageView, FollowRoomViewL, CreateAPIView):
    
    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        room_chat = request.data['room_model']
    
        if not is_user_in_room(user_id, room_chat):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        message = request.data['message']
        vid_pics = request.data.getlist('vid_pics')
        
        serializer = self.get_serializer(data={
            'room_model': room_chat,
            'profile_model': user_id,
            'message': message
        })
        
        serializer.is_valid(raise_exception=True)
        message_instance = serializer.save()
        
        vid_pic_models = []
        for vid_pic in vid_pics:
            vid_pic_instance = models.VidPicModel(mess_model=message_instance, vid_pic=vid_pic)
            vid_pic_instance.full_clean()
            vid_pic_models.append(vid_pic_instance)
        
        models.VidPicModel.objects.bulk_create(vid_pic_models)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class VidPicViewL(VidPicView, FollowMessageViewL):
    pass


class LikeViewL(LikeView, FollowMessageViewL):
    pass

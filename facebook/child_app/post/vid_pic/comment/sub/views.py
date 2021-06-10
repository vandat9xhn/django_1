from rest_framework.generics import ListAPIView
#
from .serizializers import VidPicSubSerializer, VidPicSubModel, VidPicSubLikeSerializer, VidPicSubLikeModel, \
    VidPicSubHistorySerializer, VidPicSubHistoryModel
#
from _common.views.user_create import UserCreateView

# Create your views here.


#


class VidPicSubViewLC(ListAPIView, UserCreateView):
    queryset = VidPicSubModel.objects.all()
    serializer_class = VidPicSubSerializer


#


class VidPicSubLikeViewL(ListAPIView):
    queryset = VidPicSubLikeModel.objects.all()
    serializer_class = VidPicSubLikeSerializer


#


class VidPicSubHistoryViewL(ListAPIView):
    queryset = VidPicSubHistoryModel.objects.all()
    serializer_class = VidPicSubHistorySerializer

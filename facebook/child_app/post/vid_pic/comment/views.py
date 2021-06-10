from rest_framework.generics import ListAPIView
#
from .serializers import VidPicCmtSerializer, VidPicCmtModel, VidPicCmtLikeSerializer, VidPicCmtLikeModel, \
    VidPicCmtHistorySerializer, VidPicCmtHistoryModel
#
from _common.views.user_create import UserCreateView

# Create your views here.


#


class VidPicCmtViewLC(ListAPIView, UserCreateView):
    queryset = VidPicCmtModel.objects.all()
    serializer_class = VidPicCmtSerializer


#


class VidPicCmtLikeViewL(ListAPIView):
    queryset = VidPicCmtLikeModel.objects.all()
    serializer_class = VidPicCmtLikeSerializer


#


class VidPicCmtHistoryViewL(ListAPIView):
    queryset = VidPicCmtHistoryModel.objects.all()
    serializer_class = VidPicCmtHistorySerializer

from rest_framework.generics import ListAPIView
#
from .serializers import VidPicSerializer, VidPicModel, VidPicLikeSerializer, VidPicLikeModel, VidPicShareSerializer, \
    VidPicShareModel

#


class VidPicViewL(ListAPIView):
    queryset = VidPicModel.objects.all()
    serializer_class = VidPicSerializer


class VidPicLikeViewL(ListAPIView):
    queryset = VidPicLikeModel.objects.all()
    serializer_class = VidPicLikeSerializer


class VidPicShareViewL(ListAPIView):
    queryset = VidPicShareModel.objects.all()
    serializer_class = VidPicShareSerializer

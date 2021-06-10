from rest_framework.generics import ListAPIView
#
from .serializers import LikeSerializer, LikeModel, ShareSerializer, ShareModel

#


class LikeViewL(ListAPIView):
    queryset = LikeModel.objects.all()
    serializer_class = LikeSerializer


class ShareViewL(ListAPIView):
    queryset = ShareModel.objects.all()
    serializer_class = ShareSerializer

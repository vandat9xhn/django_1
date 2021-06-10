from rest_framework.generics import ListAPIView
#
from . import models, serializers


# Create your views here.


class CartViewL(ListAPIView):
    queryset = models.CartModel.objects.all()
    serializer_class = serializers.CartSerializer


class BuyViewL(ListAPIView):
    queryset = models.BuyModel.objects.all()
    serializer_class = serializers.BuySerializer


class CancelViewL(ListAPIView):
    queryset = models.CancelModel.objects.all()
    serializer_class = serializers.CancelSerializer

from rest_framework.generics import ListAPIView
#
from . import serializers
from . import models


# Create your views here.


class ShopViewL(ListAPIView):
    queryset = models.ShopModel.objects.all()
    serializer_class = serializers.ShopSerializer

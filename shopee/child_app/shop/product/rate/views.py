from rest_framework.generics import ListAPIView
#
from . import serializers
from . import models


# Create your views here.


class ProductRateViewL(ListAPIView):
    queryset = models.ProductRateModel.objects.all()
    serializer_class = serializers.ProductRateSerializer

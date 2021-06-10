from rest_framework.generics import ListAPIView
#
from . import serializers
from . import models


# Create your views here.


class ProductCmtViewL(ListAPIView):
    queryset = models.ProductCmtModel.objects.all()
    serializer_class = serializers.ProductCmtSerializer

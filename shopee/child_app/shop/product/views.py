from rest_framework.generics import ListAPIView
#
from . import serializers
from . import models


# Create your views here.


class ProductViewL(ListAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer

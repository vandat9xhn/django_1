from rest_framework.generics import ListAPIView, RetrieveAPIView
#
from . import models, serializers
#
from _common.views.no_token import NoTokenView


# Create your views here.


# ----------------


class ShopView:
    queryset = models.ShopModel.objects.all()
    serializer_class = serializers.ShopSerializer


# ----------------


class ShopViewL(ShopView, NoTokenView, ListAPIView):
    pass


class ShopViewR(ShopView, NoTokenView, RetrieveAPIView):
    pass

from rest_framework.generics import ListAPIView
#
from . import models, serializers
#
from _common.views.no_token import NoTokenView


# Create your views here.


# ---------------


class TransportView:
    queryset = models.TransportModel.objects.all()
    serializer_class = serializers.TransportSerializer


# --------------


class TransportViewL(NoTokenView, TransportView, ListAPIView):
    pass

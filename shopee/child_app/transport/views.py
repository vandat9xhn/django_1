from rest_framework.generics import ListAPIView
#
from .serializers import TransportSerializer, TransportModel


# Create your views here.


class TransportViewL(ListAPIView):
    queryset = TransportModel.objects.all()
    serializer_class = TransportSerializer

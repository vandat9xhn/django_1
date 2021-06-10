from rest_framework.generics import ListAPIView
#
from .serializers import HistorySerializer, HistoryModel

#


class HistoryViewL(ListAPIView):
    queryset = HistoryModel.objects.all()
    serializer_class = HistorySerializer

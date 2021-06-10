from rest_framework.generics import ListAPIView
#
from .serializers import VoucherSerializer, VoucherModel


# Create your views here.


class VoucherViewL(ListAPIView):
    queryset = VoucherModel.objects.all()
    serializer_class = VoucherSerializer

from rest_framework.generics import ListAPIView
#
from . import models, serializers


# Create your views here.


class VoucherView:
    queryset = models.VoucherModel.objects.all()
    serializer_class = serializers.VoucherSerializer


# -------------


class VoucherViewL(VoucherView, ListAPIView):
    pass

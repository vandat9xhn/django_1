from rest_framework.generics import ListAPIView
#
from . import models, serializers


# Create your views here.


# ---------------


class PaymentView:
    queryset = models.PaymentModel.objects.all()
    serializer_class = serializers.PaymentSerializer


# -----------------


class PaymentViewL(PaymentView, ListAPIView):
    pass

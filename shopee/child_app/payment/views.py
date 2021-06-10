from rest_framework.generics import ListAPIView
#
from .serializers import PaymentSerializer, PaymentModel


# Create your views here.


class PaymentViewL(ListAPIView):
    queryset = PaymentModel.objects.all()
    serializer_class = PaymentSerializer

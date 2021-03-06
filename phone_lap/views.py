from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
#
from . import models, serializers
#
from _common.views.no_token import NoTokenView
#
import json

# Create your views here.


# ----------


class PhoneLapView(NoTokenView):
    queryset = models.PhoneLapModel.objects.all()
    serializer_class = serializers.PhoneLapSerializer


class VidPicView(NoTokenView):
    queryset = models.VidPicModel.objects.all()
    serializer_class = serializers.VidPicSerializer


class OrderView(NoTokenView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializer


# ----------


class PhoneLapViewL(PhoneLapView, ListAPIView):

    def get_queryset(self):
        exclude_ids = self.request.query_params.getlist('exclude_ids')
        filter_string = self.request.query_params.get('filter_string')
        # print(filter_string)
        filter_data = json.loads(filter_string) if filter_string else {}

        return self.queryset.filter(**filter_data).exclude(id__in=exclude_ids)


class PhoneLapViewR(PhoneLapView, RetrieveAPIView):
    pass


class VidPicViewL(VidPicView, ListAPIView):

    def get_queryset(self):
        phone_lap_id = self.request.query_params['phone_lap_model']

        return self.queryset.filter(phone_lap_model=phone_lap_id)


class OrderViewC(OrderView, CreateAPIView):
    pass

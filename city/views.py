from django.db.models import Q
#
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
#
from . import models, serializers
#
from _common.views.no_token import NoTokenView
from _common.views.user_create import UserCreateView
from _common.views.user_update import UserUpdateView, UserUpdateToHistoryView
from _common.views.user_delete import UserDestroyView

# Create your views here.


# -------------------


class CityView:
    queryset = models.CityModel.objects.all()
    serializer_class = serializers.CitySerializer


class HistoryView:
    queryset = models.HistoryModel.objects.all()
    serializer_class = serializers.HistorySerializer


# ------------------


#
class CityViewL(CityView, ListAPIView):

    def get_queryset(self):
        search = self.request.query_params.get('search')

        if search is None:
            search = ''

        return self.queryset.filter(
            Q(city__contains=search) |
            Q(street__contains=search) |
            Q(quote__contains=search)
        )


class CityViewNoTokenL(NoTokenView, CityViewL):
    pass


class CityViewC(CityView, UserCreateView):
    pass


class CityViewU(CityView, UserUpdateToHistoryView):

    @staticmethod
    def get_update_fields():
        return ['city', 'street', 'bg_color', 'quote', 'image']

    def handle_model_history(self, instance, data_history):
        models.HistoryModel.objects.create(
            city_model=instance,
            **data_history,
        )


class CityViewD(CityView, UserDestroyView):
    pass


#
class HistoryViewL(NoTokenView, HistoryView, ListAPIView):

    def get_queryset(self):
        city_id = self.request.query_params.get('city_model')

        return self.queryset.filter(city_model=city_id)

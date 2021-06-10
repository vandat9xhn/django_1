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
from _common.views.user_update import UserUpdateView
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


class CityViewU(CityView, UserUpdateView):

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        profile_model = instance.profile_model
        user_id = request.user.id

        if profile_model.id != user_id:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        data_history = {}

        for field in ['city', 'street', 'quote', 'image']:
            if field in data:
                old_value = getattr(instance, field)
                if data[field] != old_value:
                    data_history[field] = old_value

        if data_history == {}:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=profile_model)

        models.HistoryModel.objects.create(
            city_model=instance,
            **data_history,
        )

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(status=status.HTTP_200_OK)


class CityViewD(CityView, UserDestroyView):
    pass


#
class HistoryViewL(NoTokenView, HistoryView, ListAPIView):

    def get_queryset(self):
        city_id = self.request.query_params.get('city_model')

        return self.queryset.filter(city_model=city_id)

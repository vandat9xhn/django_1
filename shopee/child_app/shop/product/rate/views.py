from rest_framework.response import Response
from rest_framework.generics import ListAPIView
#
from _common.views.user_create import UserCreateOnlyOne
from _common.views.no_token import NoTokenView
#
from . import models, serializers


# Create your views here.


# -----------------


class ProductRateView:
    queryset = models.ProductRateModel.objects.all()
    serializer_class = serializers.ProductRateSerializer


# ----------------


class ProductRateCommonViewL(ProductRateView, ListAPIView):

    def get_queryset(self):
        product_model = self.request.query_params.get('product_model')

        return self.queryset.filter(product_model=product_model)


class ProductRateDataView(ProductRateCommonViewL):

    def get_rate_arr(self):
        queryset = self.get_queryset()

        return {'rate_arr': [
            len(queryset.filter(num_rate=5).values_list('num_rate', flat=True)),
            len(queryset.filter(num_rate=4).values_list('num_rate', flat=True)),
            len(queryset.filter(num_rate=3).values_list('num_rate', flat=True)),
            len(queryset.filter(num_rate=2).values_list('num_rate', flat=True)),
            len(queryset.filter(num_rate=1).values_list('num_rate', flat=True)),
        ]}

    def get_data_response(self):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset[0:3], many=True)

        return {'data': serializer.data, 'count': queryset.count()}

    def get(self, request, *args, **kwargs):
        data = {
            **self.get_data_response(),
            **self.get_rate_arr()
        }

        return Response(data)


# ----------


class ProductRateTokenDataView(ProductRateDataView):

    def get_data_response(self):
        queryset = self.get_queryset()
        user_rate_queryset = queryset.filter(profile_model=self.request.user.id)

        if user_rate_queryset:
            serializer_user = self.get_serializer(user_rate_queryset, many=True)
            serializer_common = self.get_serializer(
                queryset.exclude(profile_model=self.request.user.id)[0:2],
                many=True
            )
            #
            data = serializer_user.data + serializer_common.data
        else:
            serializer_common = self.get_serializer(queryset[0:3], many=True)
            #
            data = serializer_common.data

        return {'data': data, 'count': queryset.count()}


class ProductRateNoTokenDataView(ProductRateDataView):
    pass


#
class ProductRateViewL(ProductRateCommonViewL):
    pass


#
class ProductRateViewC(ProductRateView, UserCreateOnlyOne):

    def get_instance_create(self):
        user_id = self.request.user.id
        product_id = self.request.data.get('product_model')

        return self.queryset.get(profile_model=user_id, product_model=product_id)

    def handle_exists(self, instance):
        serializer = self.get_serializer(instance=instance, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

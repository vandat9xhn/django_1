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


#
class ProductRateViewL(ProductRateView, ListAPIView):

    def get_queryset(self):
        product_model = self.request.query_params.get('product_model')

        return self.queryset.filter(product_model=product_model)


class ProductRateViewNoTokenL(NoTokenView, ProductRateViewL):
    pass


class ProductRateViewC(ProductRateView, UserCreateOnlyOne):

    def get_instance_create(self):
        user_id = self.request.user.id
        product_id = self.request.data.get('product_model')

        return self.queryset.get(profile_model=user_id, product_model=product_id)

    def handle_exists(self, instance):
        serializer = self.get_serializer(instance=instance, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

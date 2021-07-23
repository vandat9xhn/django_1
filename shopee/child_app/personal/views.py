from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
#
from . import models, serializers
#
from user_profile.models import ProfileModel
from ..transport.models import TransportPriceModel
#
from _common.views.user_create import UserCreateOnlyOne
from _common.views.user_update import UserUpdateView
from _common.views.user_delete import UserDestroyView
from _common.views.user_list import UserListView


# Create your views here.


# ----------------


class CartView:
    queryset = models.CartModel.objects.all()
    serializer_class = serializers.CartSerializer


class BuyView:
    queryset = models.BuyModel.objects.all()
    serializer_class = serializers.BuySerializer


class CancelView:
    queryset = models.CancelModel.objects.all()
    serializer_class = serializers.CancelSerializer


# ----------------


#
class CartViewLC(CartView, ListAPIView, UserCreateOnlyOne):

    def get_queryset(self):
        user_id = self.request.user.id
        checked = self.request.query_params.get('checked')

        if checked is None:
            return self.queryset.filter(profile_model=user_id)

        return self.queryset.filter(profile_model=user_id, checked=True)

    def get_instance_create(self):
        user_id = self.request.user.id
        product_id = self.request.data.get('product_model')

        return self.queryset.get(profile_model=user_id, product_model=product_id)

    def handle_exists(self, instance):
        quantity = self.request.data.get('quantity')

        instance.quantity = quantity
        instance.save()


class CartViewUD(CartView, UserUpdateView, DestroyAPIView):

    def destroy(self, request, *args, **kwargs):
        user_id = request.user.id
        cart_checked_models = models.CartModel.objects.filter(profile_model=user_id, checked=True)
        cart_checked_models.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


#
class BuyViewLC(BuyView, CreateAPIView, UserListView):

    def create(self, request, *args, **kwargs):
        user_id = request.user.id
        trans_id = request.data.get('transport_price_model')
        status_buy = 'buying'

        trans_price_model = TransportPriceModel.objects.get(id=trans_id)
        data_buy = {
            'profile_model': ProfileModel.objects.get(id=user_id),
            'transport_name': trans_price_model.price,
            'trans_price': trans_price_model.price,
            'status': status_buy,
        }
        cart_checked_models = models.CartModel.objects.filter(profile_model=user_id, checked=True)

        models.BuyModel.objects.bulk_create([
            models.BuyModel(
                product_model=cart_model.product_model,
                quantity=cart_model.quantity,
                **data_buy
            ) for cart_model in cart_checked_models
        ])

        cart_checked_models.delete()

        return Response(status=status.HTTP_200_OK)


class BuyViewD(BuyView, UserDestroyView):

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.status != 'buying':
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return super().delete(request, *args, **kwargs)

    def perform_destroy(self, instance):
        data_cancel = {
            'product_model': instance.product_model,
            'quantity': instance.quantity,
            'profile_model': instance.profile_model,
        }

        instance.delete()
        models.CancelModel.objects.create(**data_cancel)


#
class CancelViewL(CartView, UserListView):
    pass

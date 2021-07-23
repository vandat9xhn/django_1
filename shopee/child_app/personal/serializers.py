from _common.serializers.data_field import FieldSerializer
#
from . import models

#


class CartSerializer(FieldSerializer):
    name_field = 'carts'
    #

    class Meta:
        model = models.CartModel
        fields = '__all__'


class BuySerializer(FieldSerializer):
    name_field = 'buys'
    #

    class Meta:
        model = models.BuyModel
        fields = '__all__'


class CancelSerializer(FieldSerializer):
    name_field = 'cancels'
    #

    class Meta:
        model = models.CancelModel
        fields = '__all__'

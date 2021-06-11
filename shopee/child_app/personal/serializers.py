from _common.serializers.data_field import FieldSerializer
#
from . import models

#


class CartSerializer(FieldSerializer):
    name_field = 'cart[]'
    #

    class Meta:
        model = models.CartModel
        fields = '__all__'


class BuySerializer(FieldSerializer):
    name_field = 'buy[]'
    #

    class Meta:
        model = models.BuyModel
        fields = '__all__'


class CancelSerializer(FieldSerializer):
    name_field = 'cancel[]'
    #

    class Meta:
        model = models.CancelModel
        fields = '__all__'

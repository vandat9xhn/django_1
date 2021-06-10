from _common.serializers.data_field import FieldSerializer
#
from . import models


#


class ProductRateSerializer(FieldSerializer):
    name_field = 'product_rates[]'
    #

    class Meta:
        model = models.ProductRateModel
        fields = '__all__'

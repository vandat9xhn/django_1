from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import FieldSerializer, DataSerializerL
#
from .models import TransportModel, TransportPriceModel

#


class TransportPriceSerializer(FieldSerializer):
    name_field = 'transport_price[]'
    #

    class Meta:
        model = TransportPriceModel
        fields = '__all__'


class TransportSerializer(DataSerializerL):
    name_field = 'transport[]'
    #
    transport_prices = SerializerMethodField()

    class Meta:
        model = TransportModel
        fields = '__all__'

    def get_transport_prices(self, instance):
        return self.get_data_l(
            TransportPriceSerializer,
            TransportPriceModel.objects.filter(transport_model=instance.id)
        )

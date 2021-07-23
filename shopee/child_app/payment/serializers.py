from _common.serializers.data_field import FieldSerializer
#
from .models import PaymentModel

#


class PaymentSerializer(FieldSerializer):
    name_field = 'payments'
    #

    class Meta:
        model = PaymentModel
        fields = '__all__'

from _common.serializers.data_field import FieldSerializer
#
from .models import VoucherModel, VoucherPaymentModel


#


class VoucherPaymentSerializer(FieldSerializer):
    name_field = 'voucher_payments[]'
    #

    class Meta:
        model = VoucherPaymentModel
        fields = '__all__'


class VoucherSerializer(FieldSerializer):
    name_field = 'vouchers[]'
    #

    class Meta:
        model = VoucherModel
        fields = '__all__'

from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import FieldSerializer
from _common.serializers.data_field import DataSerializerL
#
from .models import VoucherModel, VoucherPaymentModel


#


class VoucherPaymentSerializer(FieldSerializer):
    name_field = 'voucher_payment[]'
    #

    class Meta:
        model = VoucherPaymentModel
        fields = '__all__'


class VoucherSerializer(DataSerializerL):
    name_field = 'voucher[]'
    #
    payment = SerializerMethodField()

    class Meta:
        model = VoucherModel
        fields = '__all__'

    def get_payment(self, instance):
        return self.get_data_l(
            VoucherPaymentSerializer,
            VoucherPaymentModel.objects.filter(voucher_model=instance.id)
        )

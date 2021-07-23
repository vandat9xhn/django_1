from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import FieldSerializer, DataSerializerL
#
from . import models

#


class ShopVidPicSerializer(FieldSerializer):
    name_field = 'shop_vid_pics'

    #

    class Meta:
        model = models.ShopVidPicModel
        fields = '__all__'


class ShopVoucherPriceSerializer(FieldSerializer):
    name_field = 'shop_voucher_prices'

    #

    class Meta:
        model = models.ShopVoucherPriceModel
        fields = '__all__'


class ShopVoucherAmountSerializer(FieldSerializer):
    name_field = 'shop_voucher_amounts'

    #

    class Meta:
        model = models.ShopVoucherAmountModel
        fields = '__all__'


class ShopGiftSerializer(FieldSerializer):
    name_field = 'shop_gifts'

    #

    class Meta:
        model = models.ShopGiftModel
        fields = '__all__'


class ShopGroupSerializer(FieldSerializer):
    name_field = 'shop_group[]'

    #

    class Meta:
        model = models.ShopGroupModel
        fields = '__all__'


class ShopSerializer(DataSerializerL):
    name_field = 'shops'
    #
    vid_pics = SerializerMethodField()
    voucher_prices = SerializerMethodField()
    voucher_amounts = SerializerMethodField()
    groups = SerializerMethodField()
    gifts = SerializerMethodField()

    class Meta:
        model = models.ShopModel
        fields = '__all__'

    def get_vid_pics(self, instance):
        return self.get_data_l(
            ShopVidPicSerializer,
            models.ShopVidPicModel.objects.filter(shop_model=instance.id)
        )

    def get_voucher_prices(self, instance):
        return self.get_data_l(
            ShopVoucherPriceSerializer,
            models.ShopVoucherPriceModel.objects.filter(shop_model=instance.id)
        )

    def get_voucher_amounts(self, instance):
        return self.get_data_l(
            ShopVoucherAmountSerializer,
            models.ShopVoucherAmountModel.objects.filter(shop_model=instance.id)
        )

    def get_groups(self, instance):
        return self.get_data_l(
            ShopGroupSerializer,
            models.ShopGroupModel.objects.filter(shop_model=instance.id)
        )

    def get_gifts(self, instance):
        return self.get_data_l(
            ShopGiftSerializer,
            models.ShopGiftModel.objects.filter(shop_model=instance.id)
        )

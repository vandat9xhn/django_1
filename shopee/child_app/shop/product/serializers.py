from rest_framework.serializers import SerializerMethodField
#
from _common.serializers.data_field import FieldSerializer, DataSerializerL
#
from . import models
#
from .comment import models as comment_models, serializers as comment_serializers
from .rate import models as rate_models, serializers as rate_serializers


#


class ProductVidPicSerializer(FieldSerializer):
    name_field = 'product_vid_pics'

    #

    class Meta:
        model = models.ProductVidPicModel
        fields = '__all__'


class ProductSerializer(DataSerializerL):
    name_field = 'products'
    #
    vid_pics = SerializerMethodField()
    rates = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = models.ProductModel
        fields = '__all__'

    def get_vid_pics(self, instance):
        return self.get_data_l(
            ProductVidPicSerializer,
            models.ProductVidPicModel.objects.filter(product_model=instance.id),
            'product_vid_pic'
        )

    def get_rates(self, instance):
        return self.get_data_l(
            rate_serializers.ProductRateSerializer,
            rate_models.ProductRateModel.objects.filter(product_model=instance.id),
            'product_rate'
        )

    def get_comments(self, instance):
        return self.get_data_l(
            comment_serializers.ProductCmtSerializer,
            comment_models.ProductCmtModel.objects.filter(product_model=instance.id),
            'product_cmt'
        )
